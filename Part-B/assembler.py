#!/usr/bin/env python3
"""
Two-pass Hack assembler for the Nand2Tetris Hack platform.
Personal feature for K=94 (K mod 3 = 1):
Invalid instructions produce a clear error with the original source line number.
"""
from pathlib import Path
import argparse
import re
import sys

PREDEFINED = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
}
for i in range(16):
    PREDEFINED[f"R{i}"] = i

DEST = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111",
}
JUMP = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
}
COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001", "!M": "1110001",
    "-D": "0001111", "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
    "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101",
}

LABEL_RE = re.compile(r"^\(([A-Za-z_.$:][\w.$:]*)\)$")
SYMBOL_RE = re.compile(r"^[A-Za-z_.$:][\w.$:]*$")

class AssemblyError(Exception):
    pass

def clean_source(path):
    result = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("//", 1)[0].strip()
        if line:
            result.append((line_no, re.sub(r"\s+", "", line)))
    return result

def first_pass(lines):
    symbols = dict(PREDEFINED)
    instructions = []
    rom_address = 0
    for line_no, line in lines:
        if line.startswith("(") and line.endswith(")"):
            match = LABEL_RE.match(line)
            if not match:
                raise AssemblyError(f"Line {line_no}: invalid label declaration")
            label = match.group(1)
            if label in symbols:
                raise AssemblyError(f"Line {line_no}: label '{label}' conflicts with an existing symbol")
            symbols[label] = rom_address
        else:
            instructions.append((line_no, line))
            rom_address += 1
    return symbols, instructions

def encode_c_instruction(line, line_no):
    if line.count("=") > 1 or line.count(";") > 1:
        raise AssemblyError(f"Line {line_no}: invalid instruction")
    if "=" in line:
        dest, rest = line.split("=", 1)
    else:
        dest, rest = "", line
    if ";" in rest:
        comp, jump = rest.split(";", 1)
    else:
        comp, jump = rest, ""
    if dest not in DEST or comp not in COMP or jump not in JUMP:
        raise AssemblyError(f"Line {line_no}: invalid instruction")
    return "111" + COMP[comp] + DEST[dest] + JUMP[jump]

def assemble(path):
    lines = clean_source(path)
    symbols, instructions = first_pass(lines)
    next_variable = 16
    machine = []

    for line_no, line in instructions:
        if line.startswith("@"):
            symbol = line[1:]
            if not symbol:
                raise AssemblyError(f"Line {line_no}: invalid instruction")
            if symbol.isdigit():
                value = int(symbol)
                if value > 32767:
                    raise AssemblyError(f"Line {line_no}: A-instruction value out of range")
            elif SYMBOL_RE.match(symbol):
                if symbol not in symbols:
                    symbols[symbol] = next_variable
                    next_variable += 1
                value = symbols[symbol]
            else:
                raise AssemblyError(f"Line {line_no}: invalid instruction")
            machine.append(f"{value:016b}")
        else:
            machine.append(encode_c_instruction(line, line_no))

    return machine, symbols

def main():
    parser = argparse.ArgumentParser(description="Assemble Hack .asm source into .hack machine code.")
    parser.add_argument("input", help="Input .asm file")
    parser.add_argument("-o", "--output", help="Output .hack file (default: same name)")
    parser.add_argument("--symbols", action="store_true",
                        help="Also write symbols.txt (optional; K=94 feature is line-numbered errors)")
    args = parser.parse_args()

    source = Path(args.input)
    if not source.exists():
        print(f"Error: file not found: {source}", file=sys.stderr)
        return 1
    output = Path(args.output) if args.output else source.with_suffix(".hack")

    try:
        machine, symbols = assemble(source)
    except AssemblyError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    output.write_text("\n".join(machine) + "\n", encoding="utf-8")
    if args.symbols:
        symbol_path = output.parent / "symbols.txt"
        symbol_path.write_text(
            "\n".join(f"{name} {address}" for name, address in sorted(symbols.items())) + "\n",
            encoding="utf-8"
        )
    print(f"Assembly successful: {len(machine)} instructions -> {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

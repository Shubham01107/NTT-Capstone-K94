NAND TO TETRIS CAPSTONE STARTER PACKAGE — K = 94
================================================

IMPORTANT
---------
This ZIP contains a complete starter implementation for your capstone files.
It does NOT contain the official Nand2Tetris simulator or official test scripts.
Use the Nand2Tetris Online IDE for HDL simulation and CPU emulation.

YOUR PERSONAL SETTINGS
----------------------
K = 94
K mod 3 = 1: assembler prints clear invalid-instruction errors with source line numbers.
K mod 4 = 2: box width = 48 pixels = 3 words per row.
Starting row = 94
Height = 20 rows (rows 94 through 113)
Starting screen address = 16384 + 32*94 = 19392

FOLDER CONTENTS
---------------
Part-A/
  CPU.hdl
  Memory.hdl
  Computer.hdl
Part-B/
  assembler.py
  test-programs/     (put official Add.asm, Max.asm, Rect.asm, Pong.asm here)
  output/
Part-C/
  Box.asm
  Box.hack
Report/
  Project_Report_Template.md
  screenshots/
README_FIRST.txt

WHAT TO DO FIRST
----------------
1. Extract this ZIP.
2. Open the extracted NTT_Capstone_K94 folder in VS Code.
3. Open Part-B/assembler.py and Part-C/Box.asm if you want to inspect them.
4. In the terminal, run:
       python Part-B/assembler.py Part-C/Box.asm
   This creates Part-C/Box.hack.
5. In the Nand2Tetris Online IDE, use the Hardware Simulator for the HDL files.
   The online IDE has its own project/file workspace. Upload or copy the HDL files
   into the corresponding Project 5 files there, then run the supplied tests.
6. Use the CPU Emulator to load Box.hack and test keyboard press/release.

HDL NOTE
--------
The HDL files below use the standard Hack chip interfaces and standard built-in
chips (ALU, Register, PC, RAM16K, Screen, Keyboard, ROM32K, etc.).
If your course requires your own earlier chips, replace built-ins with your
working implementations where appropriate and document any built-in chips used.

TEST NOTE
---------
The official test files and compare files are not bundled here. Obtain them from
the official Nand2Tetris course/project materials or your Online IDE workspace.
Test Add.asm, Max.asm, Rect.asm, and Pong.asm using your own assembler, then
compare the generated .hack files with the official assembler output.

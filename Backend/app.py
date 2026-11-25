
from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import subprocess
import sys

app = Flask(__name__)

# Main project folder
ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = ROOT / "Dashboard"

# Actual project files allowed to be accessed
ALLOWED_FILES = {
    "CPU.hdl": ROOT / "Part-A" / "CPU.hdl",
    "Memory.hdl": ROOT / "Part-A" / "Memory.hdl",
    "Computer.hdl": ROOT / "Part-A" / "Computer.hdl",
    "assembler.py": ROOT / "Part-B" / "assembler.py",
    "Box.asm": ROOT / "Part-C" / "Box.asm",
    "Box.hack": ROOT / "Part-C" / "Box.hack",
}


# Open main dashboard
@app.route("/")
def dashboard():
    return send_from_directory(DASHBOARD, "index.html")


# Load dashboard assets
@app.route("/<path:filename>")
def dashboard_files(filename):
    return send_from_directory(DASHBOARD, filename)


# Read actual project files
@app.route("/api/files/<filename>")
def get_file(filename):
    path = ALLOWED_FILES.get(filename)

    if not path or not path.is_file():
        return jsonify({
            "success": False,
            "error": "File not found"
        }), 404

    try:
        return jsonify({
            "success": True,
            "filename": filename,
            "code": path.read_text(encoding="utf-8")
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# Run the actual Python assembler
@app.route("/api/assemble", methods=["POST"])
def assemble():

    assembler = ROOT / "Part-B" / "assembler.py"
    program = ROOT / "Part-C" / "Box.asm"
    hack_file = ROOT / "Part-C" / "Box.hack"

    if not assembler.is_file():
        return jsonify({
            "success": False,
            "error": "assembler.py not found"
        }), 404

    if not program.is_file():
        return jsonify({
            "success": False,
            "error": "Box.asm not found"
        }), 404

    try:
        result = subprocess.run(
            [sys.executable, str(assembler), str(program)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30
        )

        machine_code = ""

        if result.returncode == 0 and hack_file.exists():
            machine_code = hack_file.read_text(
                encoding="utf-8"
            )

        return jsonify({
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "machine_code": machine_code
        })

    except subprocess.TimeoutExpired:
        return jsonify({
            "success": False,
            "error": "Assembly timed out"
        }), 500

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# Start Flask server
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

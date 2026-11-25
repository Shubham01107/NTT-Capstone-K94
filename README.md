# Nand2Tetris Capstone Project – K94

A custom Hack Computer implementation and a Python-based assembler, featuring an interactive dashboard and a keyboard-controlled rectangle drawing program.

## Project Overview

This project is based on the Nand2Tetris computer architecture. It covers the implementation of Hack computer hardware components, a two-pass assembler written in Python, and an assembly program that draws a rectangle on the Hack screen.

The project also includes a web-based dashboard powered by Flask for exploring project files and running the assembler.

## Key Features

- **Hack Computer Hardware:** CPU, Memory and Computer HDL files.
- **Python Assembler:** Two-pass assembler supporting A-instructions, C-instructions, labels and variables.
- **Invalid Instruction Handling:** Reports invalid instructions with their original source line numbers.
- **Box Drawing Program:** Draws and clears a rectangle based on keyboard input.
- **Interactive Dashboard:** Web interface for viewing project files and assembling the program.
- **Flask Backend:** Connects the dashboard with the Python assembler.

## Roll Number Configuration

The project uses **K = 94** according to the assigned capstone specifications.

| Specification | Configuration |
|---|---|
| Roll Number (K) | 94 |
| K mod 3 | 1 |
| K mod 4 | 2 |
| Rectangle Width | 48 pixels |
| Rectangle Height | 20 rows |
| Starting Screen Row | 94 |
| Ending Screen Row | 113 |
| First Screen Memory Address | 19392 |

## Technologies Used

- Python 3.12
- Flask
- Hack Assembly Language
- HDL (Hardware Description Language)
- HTML5
- CSS3
- JavaScript
- Git and GitHub

## Project Structure

```text
NTT_Capstone_K94/
│
├── Backend/
│   └── app.py
│
├── Dashboard/
│   └── index.html
│
├── Part-A/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   └── Computer.hdl
│
├── Part-B/
│   ├── assembler.py
│   ├── output/
│   └── test-programs/
│
├── Part-C/
│   ├── Box.asm
│   └── Box.hack
│
├── Report/
│   ├── Project_Report_Template.md
│   └── screenshots/
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shubham01107/NTT-Capstone-K94.git
```

### 2. Open the Project Folder

```bash
cd NTT-Capstone-K94
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Start the Dashboard

```bash
python Backend/app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## Running the Assembler

Run the following command from the project root:

```bash
python Part-B/assembler.py Part-C/Box.asm
```

The generated machine code is saved in:

```text
Part-C/Box.hack
```

## Box Drawing Specifications

The `Box.asm` program uses the assigned roll number configuration to draw a rectangle on the Hack screen.

- Press the designated keyboard key to draw the rectangle.
- Release the key to clear the rectangle.
- Rectangle dimensions: 48 pixels × 20 rows.
- Starting screen row: 94.

## Author

**Shubham Gautam**

B.Tech – Computer Science and Engineering (AI & ML)

KR Mangalam University

## Repository

[GitHub – NTT-Capstone-K94](https://github.com/Shubham01107/NTT-Capstone-K94)
# Capstone Project: Make the Computer Draw a Box

**Course:** Nand to Tetris – I (ETCNTC301)  
**University:** K.R. Mangalam University  
**Name:** ____________________  
**University Roll Number:** ____________________  
**Personal Number (K):** 94  

## 1. Project Objective
The objective is to build and test the Hack computer, create a two-pass Python assembler, and write a Hack Assembly program that displays a black rectangular box while a keyboard key is pressed.

## 2. Part A – Hack Computer
Describe the purpose and connections of CPU.hdl, Memory.hdl and Computer.hdl. Mention any built-in chips used. Add screenshots of successful official HDL tests here.

**Screenshots:**  
- CPU test: [Insert screenshot]  
- Memory test: [Insert screenshot]  
- Computer tests: [Insert screenshot]

## 3. Part B – Python Assembler
The assembler performs two passes. In the first pass it removes comments and blank lines, records labels and their ROM addresses, and counts instructions. In the second pass it converts A-instructions and C-instructions into 16-bit binary machine instructions. New variables are assigned RAM addresses beginning at 16.

**Personal feature:** K mod 3 = 94 mod 3 = 1. Therefore, invalid instructions produce a clear error message containing the original source line number.

**Testing:** Add.asm, Max.asm, Rect.asm and Pong.asm. Insert evidence that each generated .hack file matches the official assembler output.

## 4. Part C – Box Program
K = 94.  
Starting row = 94.  
Height = 20 rows (rows 94–113).  
Width = 16 × ((94 mod 4) + 1) = 16 × 3 = 48 pixels.  
Words per row = 48 / 16 = 3.  
First screen address = 16384 + 32 × 94 = 19392.

The program continuously checks KBD. If a key is pressed, it writes -1 to three screen words for each of 20 rows. If no key is pressed, it writes 0 to those same screen words.

**Screenshot of working box:** [Insert CPU Emulator screenshot]

## 5. Programming Mistake and Correction
Describe one real mistake you encountered, the error message or unexpected result, and the exact change you made to correct it. Do not invent a mistake; write about one you actually experienced.

## 6. Conclusion
Summarize what you implemented and tested. Mention any limitations or built-in chips used.

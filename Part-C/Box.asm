// Box for K=94: starts at row 94, height 20, width 48 pixels (3 words).
// Any key pressed: draw black. No key pressed: clear the same rectangle.

(LOOP)
@KBD
D=M
@DRAW
D;JNE

// No key pressed: clear the rectangle.
@19392
D=A
@PTR
M=D
@20
D=A
@ROWS
M=D

(CLEAR_ROW)
@3
D=A
@WORDS
M=D

(CLEAR_WORD)
@PTR
A=M
M=0
@PTR
M=M+1
@WORDS
MD=M-1
@CLEAR_WORD
D;JGT

@29
D=A
@PTR
M=D+M
@ROWS
MD=M-1
@CLEAR_ROW
D;JGT
@LOOP
0;JMP

// A key is pressed: draw the rectangle.
(DRAW)
@19392
D=A
@PTR
M=D
@20
D=A
@ROWS
M=D

(DRAW_ROW)
@3
D=A
@WORDS
M=D

(DRAW_WORD)
@PTR
A=M
M=-1
@PTR
M=M+1
@WORDS
MD=M-1
@DRAW_WORD
D;JGT

@29
D=A
@PTR
M=D+M
@ROWS
MD=M-1
@DRAW_ROW
D;JGT

@LOOP
0;JMP

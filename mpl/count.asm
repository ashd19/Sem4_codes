.MODEL SMALL
.STACK 100H
.DATA
    num     DB 0F3h       ; Example number = 11110011 (243 in decimal)
    ones    DB 0          ; Counter for 1s
    zeros   DB 0          ; Counter for 0s

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV AL, num      ; Load the 8-bit number
    MOV CL, 8        ; Set loop counter for 8 bits

    MOV BL, 0        ; ones = 0
    MOV BH, 0        ; zeros = 0

CHECK_BIT:
    ROL AL, 1        ; Rotate left to bring MSB to Carry Flag
    JC IS_ONE        ; If Carry is 1, it's a 1 bit

IS_ZERO:
    INC BH           ; Increment zero counter
    JMP NEXT

IS_ONE:
    INC BL           ; Increment one counter

NEXT:
    DEC CL           ; Decrement bit counter
    JNZ CHECK_BIT    ; Loop until all 8 bits checked

    ; Store result in memory variables
    MOV ones, BL     ; Number of 1s
    MOV zeros, BH    ; Number of 0s

    ; Exit
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN

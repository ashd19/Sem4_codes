.MODEL SMALL
.STACK 100H
.DATA
    NUMBERS DB 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
    N       DB 10        ; total numbers
.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV SI, 0        ; index pointer
    MOV CH, 0        ; EVENN counter
    MOV CL, 0        ; odd counter
    MOV BL, N

NEXT_NUM:
    MOV AL, NUMBERS[SI]
    TEST AL, 1       ; check LSB (1 = odd, 0 = EVENN)
    JZ EVENN
    INC CL           ; odd count++
    JMP CONT
EVENN:
    INC CH           ; EVENN count++
CONT:
    INC SI
    DEC BL
    JNZ NEXT_NUM

    ; Now CH = EVENN count, CL = odd count

    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN

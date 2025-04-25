.MODEL SMALL
.STACK 100H
.DATA
    STR DB "MADAM", 0   ; input string, null-terminated
    IS_PAL DB 0         ; 1 = palindrome, 0 = not

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Find string length
    LEA SI, STR
    MOV CX, 0
FIND_LEN:
    CMP BYTE PTR [SI], 0
    JE LENGTH_FOUND
    INC CX
    INC SI
    JMP FIND_LEN
LENGTH_FOUND:
    ; Now CX = length of string
    MOV SI, 0           ; Start index
    MOV DI, CX
    DEC DI              ; End index (0-based)

    MOV BL, 1           ; Assume palindrome
COMPARE_LOOP:
    MOV AL, STR[SI]
    MOV AH, STR[DI]
    CMP AL, AH
    JNE NOT_PALINDROME

    INC SI
    DEC DI
    CMP SI, DI
    JAE DONE_CHECK      ; If start >= end, we’re done
    JMP COMPARE_LOOP

NOT_PALINDROME:
    MOV BL, 0           ; Not a palindrome

DONE_CHECK:
    MOV IS_PAL, BL      ; Store result in memory
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN

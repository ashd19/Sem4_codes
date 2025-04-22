.MODEL SMALL
.STACK 100H
.DATA
    n DB 5   ; Input number (Change this value to compute factorial for other numbers)
    fact DW 1 ; Store factorial result (initialized to 1)
    msg DB "Factorial: $"

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Display Message
    MOV DX, OFFSET msg
    MOV AH, 9
    INT 21H

    ; Calculate Factorial
    MOV AL, n       ; Load 'n' into AL
    CBW             ; Convert byte to word (AL -> AX)
    CALL FACTORIAL_PROC

    ; Display Factorial Result
    CALL DISPLAY_RESULT

    ; Exit Program
    MOV AH, 4CH
    INT 21H
MAIN ENDP

; ---------------- Factorial Procedure ----------------
FACTORIAL_PROC PROC
    MOV CX, AX  ; Store 'n' in CX (loop counter)
    MOV AX, 1   ; Initialize factorial result
    MOV DX, 0   ; Clear upper part of result

FACTORIAL_LOOP:
    MUL CX      ; AX = AX * CX (Multiply and store in AX)
    LOOP FACTORIAL_LOOP  ; Decrease CX and repeat until CX = 0
    RET
FACTORIAL_PROC ENDP

; ---------------- Display Result Procedure ----------------
DISPLAY_RESULT PROC
    MOV CX, 10   ; Convert number to string
    MOV BX, 10
    MOV SI, OFFSET msg + 10  ; Buffer for digits

CONVERT_LOOP:
    MOV DX, 0
    DIV BX      ; AX / 10, remainder in DX
    ADD DL, '0' ; Convert remainder to ASCII
    DEC SI
    MOV [SI], DL
    CMP AX, 0
    JNE CONVERT_LOOP

    ; Print number
    MOV DX, SI
    MOV AH, 9
    INT 21H
    RET
DISPLAY_RESULT ENDP

END MAIN

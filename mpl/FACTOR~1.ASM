.MODEL SMALL
.STACK 100H

.DATA
    NUM DB 5           ; Number to find factorial of
    RESULT DW 1        ; Final result (WORD size for factorial > 255)

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV AL, NUM        ; Load number
    CBW                ; Convert to word (AL -> AX)
    CALL FACTORIAL     ; Call factorial procedure

    MOV RESULT, AX     ; Store the result in memory

    MOV AH, 4CH
    INT 21H
MAIN ENDP

;--------------------------------------------------
; PROCEDURE TO CALCULATE FACTORIAL
; Input: AX = number
; Output: AX = factorial
;--------------------------------------------------
FACTORIAL PROC
    CMP AX, 1
    JBE END_FACT       ; If AX <= 1, return 1

    PUSH AX            ; Save AX (current number)
    DEC AX
    CALL FACTORIAL     ; Recursive call with AX-1
    POP BX             ; Get original AX
    MUL BX             ; AX = AX * BX

END_FACT:
    RET
FACTORIAL ENDP

END MAIN

.MODEL SMALL
.STACK 100H
.DATA
    DIGITS DB 00H, 01H, 02H, 03H, 04H, 05H, 06H, 07H, 08H, 09H ; BCD values

.CODE
MAIN PROC
    MOV AX, @DATA  ; Load data segment
    MOV DS, AX
    MOV DX, 300H   ; Address of 8255 Port A

    MOV CX, 10     ; Loop to display digits 0-9
    MOV SI, 0      ; Start index for digit array

DISPLAY_LOOP:
    MOV AL, DIGITS[SI] ; Load BCD digit
    OUT DX, AL         ; Send to 8255 (connected to 7447 decoder)
    CALL DELAY         ; Small delay for display visibility
    INC SI             ; Next digit
    LOOP DISPLAY_LOOP  ; Repeat for next digit

    ; Exit program
    MOV AH, 4CH
    INT 21H

MAIN ENDP

; Delay Procedure
DELAY PROC
    MOV CX, 0FFFFH
DELAY_LOOP:
    LOOP DELAY_LOOP
    RET
DELAY ENDP

END MAIN

.MODEL SMALL
.STACK 100H

.DATA
    PACKED_BCD     DB 42H      ; Example: packed BCD value
    UNPACKED_HIGH  DB ?        ; To store 04
    UNPACKED_LOW   DB ?        ; To store 02

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Get upper digit (high nibble)
    MOV AL, PACKED_BCD
    MOV AH, AL
    AND AH, 0F0H           ; Mask upper nibble
    MOV CL, 4              ; Load rotate count in CL
    SHR AH, CL             ; SHR AH, 4

    MOV UNPACKED_HIGH, AH

    ; Get lower digit (low nibble)
    MOV AL, PACKED_BCD
    AND AL, 0FH
    MOV UNPACKED_LOW, AL

    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN

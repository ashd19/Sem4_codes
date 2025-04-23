.MODEL SMALL
.STACK 100H

.DATA
source      DB 10, 20, 30, 40, 50, 60, 70, 80, 90, 100  ; Source memory block
count       DB 10                                      ; Number of elements
destination DB 10 DUP(0)                               ; Destination block (empty, filled with 0)

.CODE
MAIN PROC
    MOV AX, @DATA   ; Initialize data segment
    MOV DS, AX
    MOV ES, AX      ; Use same segment for destination

    MOV SI, OFFSET source       ; Source index pointer
    MOV DI, OFFSET destination  ; Destination index pointer
    MOV CL, count               ; Number of bytes to copy
    MOV CH, 0                   ; Clear upper byte of CX (total in CX)

COPY_LOOP:
    MOV AL, [SI]     ; Load byte from source
    MOV [DI], AL     ; Store it in destination
    INC SI           ; Move to next byte in source
    INC DI           ; Move to next byte in destination
    LOOP COPY_LOOP   ; Decrease CX and loop until 0

    MOV AH, 4CH      ; Exit to DOS
    INT 21H
MAIN ENDP
END MAIN

.MODEL SMALL
.STACK 100H
.DATA
    srcList DB 5, 12, 7, 8, 19, 24, 33, 42, 50, 17  ; Source block of numbers
    count DB 10                                     ; Number of elements
    destList DB 10 DUP(?)                           ; Destination block (uninitialized)

.CODE
MAIN PROC
    MOV AX, @DATA    ; Load data segment
    MOV DS, AX
    MOV ES, AX       ; ES used for destination memory block

    MOV SI, OFFSET srcList   ; Source index
    MOV DI, OFFSET destList  ; Destination index
    MOV AL, count  
	MOV AH, 0      
	MOV CX, AX     


COPY_LOOP:
    MOV AL, [SI]   ; Load value from source
    MOV [DI], AL   ; Store value in destination
    INC SI         ; Increment source index
    INC DI         ; Increment destination index
    LOOP COPY_LOOP ; Repeat until CX = 0

    ; Exit Program
    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN

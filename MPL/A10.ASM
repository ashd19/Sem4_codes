.MODEL SMALL
.STACK 100H
.DATA
    str DB "FOLDER$", 0  ; Input string (change as needed)
    len DW 5            ; Length of string (excluding '$')
    msg1 DB "Palindrome$"
    msg2 DB "Not a Palindrome$"

.CODE
MAIN PROC                              
    MOV AX, @DATA      ; Load data segment
    MOV DS, AX

    MOV SI, OFFSET str  ; SI points to start of string
    MOV CX, len         ; CX holds length of string
    DEC CX              ; Adjust for last index (0-based)
    ADD SI, CX          ; Move SI to last character
    MOV DI, OFFSET str  ; DI points to first character

CHECK_LOOP:
    MOV AL, [DI]        ; Load character from start
    MOV BL, [SI]        ; Load character from end
    CMP AL, BL          ; Compare characters
    JNE NOT_PALINDROME  ; If mismatch, not a palindrome

    INC DI              ; Move DI forward
    DEC SI              ; Move SI backward
    CMP DI, SI          ; Check if pointers crossed
    JAE PALINDROME      ; If crossed, it's a palindrome
    JMP CHECK_LOOP      ; Repeat loop
                                      
PALINDROME:
    MOV DX, OFFSET msg1
    JMP PRINT_RESULT                 

NOT_PALINDROME:
    MOV DX, OFFSET msg2

PRINT_RESULT:
    MOV AH, 9           ; Print string
    INT 21H

    MOV AH, 4CH         ; Exit program
    INT 21H

MAIN ENDP
END MAIN

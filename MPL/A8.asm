.model small      ; Use small memory model
.stack 100h       ; Reserve 256 bytes for stack

.data
    num db 67h    ; The number to analyze (01100111 in binary)
    zeros db 0     ; Counter for 0 bits (initialize to 0)
    ones db 0      ; Counter for 1 bits (initialize to 0)

.code
main proc
    ; Set up data segment
    mov ax, @data
    mov ds, ax
    
    ; Initialize counters (FIXED: Added this missing initialization)
    mov zeros, 0
    mov ones, 0
    
    ; Prepare for bit checking
    mov al, num    ; Load our number into AL (67h = 01100111)
    mov cx, 08h    ; We'll check all 8 bits (CX = 8)
    
bit_check_loop:
    ; Rotate right through carry (puts rightmost bit in Carry Flag)
    ror al, 1      ; Example first rotation: 01100111 -> 10110011 with CF=1
    
    ; Check if the bit was 1 (Carry Flag set) or 0
    jc bit_was_one  ; Jump if CF=1
    
    ; If we get here, the bit was 0
    inc zeros       ; zeros++
    jmp next_bit    ; Skip the "one" counting
    
bit_was_one:
    ; The bit was 1
    inc ones        ; ones++
    
next_bit:
    ; Continue looping until all bits checked
    loop bit_check_loop
    
    ; Exit to DOS
    mov ah, 4Ch     ; DOS function to exit program
    int 21h         ; Call DOS interrupt
main endp
end main
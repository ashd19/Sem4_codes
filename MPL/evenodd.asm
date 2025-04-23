.model small
.stack 100h

.data
    array db 11h, 22h, 33h, 44h, 55h, 66h, 77h, 88h, 99h, 0AAh  ; Test array
    even_ptr dw 2000h  ; Where even numbers will be stored
    odd_ptr  dw 2009h  ; Where odd numbers will be stored

.code
main proc
    mov ax, @data
    mov ds, ax       ; Set up data segment

    mov si, offset array   ; SI = pointer to array start
    mov di, even_ptr       ; DI = where evens go (2000h)
    mov bx, odd_ptr        ; BX = where odds go (2009h)
    mov cx, 10            ; Loop counter (10 numbers)

check_loop:
    mov al, [si]          ; Load current number
    test al, 01h          ; Check LSB (Least Significant Bit)
    jz is_even            ; If LSB=0 (even), jump

is_odd:
    mov [bx], al          ; Store odd number at [BX]
    inc bx                ; Move odd pointer forward
    jmp next_num

is_even:
    mov [di], al          ; Store even number at [DI]
    inc di                ; Move even pointer forward

next_num:
    inc si                ; Move to next array element
    loop check_loop       ; Repeat until CX=0

    ; Exit program
    mov ax, 4C00h
    int 21h
main endp
end main
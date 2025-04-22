.model small       ; Memory model directive
.stack 100h       ; Stack segment declaration

.data
a dw 3688h        ; First BCD number (36 in upper byte, 88 in lower)
b dw 4789h        ; Second BCD number (47 in upper byte, 89 in lower)

.code
main proc
    mov ax, @data ; Initialize data segment
    mov ds, ax
    
    mov ax, a     ; Load first number into AX (3688h)
    mov bx, b     ; Load second number into BX (4789h)
    
    ; Add low bytes (BCD addition)
    add al, bl    ; AL = 88h + 89h
    daa           ; Decimal adjust (result: 77h with CF=1)
    
    mov bl, al    ; Store low byte result
    
    ; Add high bytes with carry
    mov al, ah    ; Move high byte to AL (36h)
    adc al, bh    ; Add with carry (36h + 47h + CF)
    daa           ; Decimal adjust (result: 84h)
    
    mov bh, al    ; Final high byte
    mov ah, bl    ; Final low byte
    
    ; Exit to DOS
    mov ax, 4C00h
    int 21h
main endp
end main
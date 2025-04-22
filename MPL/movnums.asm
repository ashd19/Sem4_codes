.model small 
.stack 100h 
.data 
source db 10h,20h,30h,40h,50h
.CODE
main Proc
mov ax,@data
mov ds,ax
mov si, offset source
mov di,3000h
mov cx,05h

copy_loop:
mov bl,[si]
mov [di],bl
inc si
inc di
dec cx
jnz copy_loop


mov ax,4C00h
int 21h 
main ENDP
end main
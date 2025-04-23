.model small       
.stack 100h       
.data
    a db 27h      
.code
main proc
    mov ax, @data  
    mov ds, ax    

   
    mov al, a      
    and al, 0F0h   
    ror al, 4     
    mov bl, al    

   
    mov al, a    
    and al, 0Fh    
    mov cl, al     

    ; --- THE END ---
    mov ax, 4C00h  
    int 21h        ; Close the program
main endp
end main
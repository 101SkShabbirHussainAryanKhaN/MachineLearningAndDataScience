.model small
.stack 100h
.data
    arr db 2,8,11,21
.code
main:
     mov ax ,@data
     mov ds , ax
     mov si , offset arr
     mov dx , [si]
     
     
     ;mov ah ,2
     ;int 21h 
     
     ;mov ah, 4ch 
     ;int 21h
      
     mov cx , 4
     
     l1:
        mov cx, [si]  
        add dx ,48
        inc si
        mov ah, 2
        int 21h 
        
     loop l1   
     
     mov ah, 4ch 
     int 21h

end main 
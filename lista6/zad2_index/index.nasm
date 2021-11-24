global _start

section .text

_start:
    jmp MESSAGE         ;Skaczemy do naszej wiadomości 

GOBACK:
    mov eax, 0x4        ;Wkładamy do eax 4 (syscall write)
    mov ebx, 0x1        ;Wkładamy do ebx 1
    pop ecx             ;Ściąga ze stosu adres naszej wiadomości    
                     
    mov edx, 0x7        ;Wkładamy do edx długość wiadomości
    int 0x80            ;Wywołujemy syscall write

    mov eax, 0x1
    mov ebx, 0x0
    int 0x80            ;Wywołujemy syscall exit

MESSAGE:
    call GOBACK         ;Call zapamiętuje na stacu adres następnej instrukcji (w tym wypadku jest to adres naszej wiadomości) 
                        ;i następnie skacze do GOBACK.                                      
    db "250083" , 0ah

section .data
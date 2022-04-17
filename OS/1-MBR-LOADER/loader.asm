%include "boot.inc"
SECTION LOADER vstart=LOADER_BASE_ADDR

; 实模式打印方式一
mov byte [gs:0xa0],'L'
mov byte [gs:0xa2],'O'
mov byte [gs:0xa4],'A'
mov byte [gs:0xa6],'D'
mov byte [gs:0xa8],'E'
mov byte [gs:0xaa],'R'


; 实模式打印方式二
mov si, msg
call print  ; 调用打印函数

jmp $


; 打印函数
print:
    mov ah, 0x0e
.next:
    mov al, [si]
    cmp al, 0
    jz .done
    int 0x10; 实模式下的BIOS中断
    inc si
    jmp .next
.done:
    ret

msg:
    db "Loading...", 10, 13, 0




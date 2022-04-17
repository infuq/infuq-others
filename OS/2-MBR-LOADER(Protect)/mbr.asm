; 主引导程序
;-----------------------------------------------
%include "boot.inc"
SECTION MBR vstart=0x7c00

    mov ax, cs
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov fs, ax
    mov sp, 0x7c00
    mov ax, 0xb800
    mov gs, ax

; 清屏
;---------------------------------------------------
    mov ax, 0600h
    mov bx, 0700h
    mov cx, 0
    mov dx, 184fh
    int 10h

    ; 显示"MBR"
    mov byte [gs:0x00], '1'
    mov byte [gs:0x01], 0xA4

    mov byte [gs:0x02], ' '
    mov byte [gs:0x03], 0xA4

    mov byte [gs:0x04], 'M'
    mov byte [gs:0x05], 0xA4

    mov byte [gs:0x06], 'B'
    mov byte [gs:0x07], 0xA4

    mov byte [gs:0x08], 'A'
    mov byte [gs:0x09], 0xA4


    ; 读取磁盘loader
    mov edi, 0x900  ; 读取到目标内存地址
    mov ecx, 0x2    ; 起始扇区
    mov bl, 4       ; 扇区数量. 读取4个扇区. 之所以要读取4个扇区,是因为我们把loader.bin文件写到4个扇区中了,具体查看`makefile`
    call read_disk
    
    ; 直接跳到loader的(起始代码+0x26)位置处执行
    jmp LOADER_BASE_ADDR + 0x26


; edi 读取到目标内存地址
; ecx 存储起始扇区
; bl  存储扇区数量
read_disk:

    
    ; 设置读扇区的数量
    mov dx, 0x1F2
    mov al, bl
    out dx, al

    ; 起始扇区的前八位
    mov dx, 0x1F3
    mov al, cl
    out dx, al
    
    ; 起始扇区的中八位
    mov dx, 0x1F4
    shr ecx, 8 ; ecx >> 8
    mov al, cl
    out dx, al

    ; 起始扇区的高八位
    mov dx, 0x1F5
    shr ecx, 8 ; ecx >> 8
    mov al, cl
    out dx, al

    mov dx, 0x1F6
    shr ecx, 8
    and cl, 0b1111
    mov al, 0b1110_0000; 操作主盘, LBA模式
    or al, cl
    out dx, al

    ; 设置读磁盘
    mov dx, 0x1F7
    mov al, 0x20
    out dx, al


    xor ecx, ecx; 将 ecx 清空
    mov cl, bl; 读扇区的数量

    .read:
        push cx
        call .waits;等待数据准备完毕
        call .reads;读取一个扇区
        pop cx
        loop .read

    ret


    .waits:
        mov dx, 0x1F7
        .check
            in al, dx
            jmp $+2; nop 直接跳转到下一行
            jmp $+2; 一点点延迟
            jmp $+2
            and al, 0b1000_1000; 取出第3位和第7位, 第3位表示数据是否准备完毕, 第7位表示磁盘是否繁忙
            cmp al, 0b0000_1000; 如果相等则表示数据已准备完毕且磁盘不繁忙
            jnz .check
        ret

    ; 读取一个扇区
    .reads:
        mov dx, 0x1F0
        mov cx, 256; 一个扇区512字节, 即256字(1个字等于2个字节)
        .readw:
            in ax, dx; 将端口0x1F0数据读取到ax寄存器, 每次读取2个字节
            mov [edi], ax
            add edi, 2
            loop .readw
        ret





times 510-($-$$) db 0
db 0x55, 0xaa

%include "boot.inc"
SECTION LOADER vstart=LOADER_BASE_ADDR

mov byte [gs:0xa0],'L'
mov byte [gs:0xa2],'O'
mov byte [gs:0xa4],'A'
mov byte [gs:0xa6],'D'
mov byte [gs:0xa8],'E'
mov byte [gs:0xaa],'R'

jmp $
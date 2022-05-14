assume cs:code
code segment
start:
	; 取得月份数据
	mov al,8
	out 70h,al
	in al,71h
	
	; 分离月份的十, 个位
	mov ah,al
	mov cl,4
	shr ah,cl
	and al,00001111b
	
	; 转换为ASCII码
	add ah,30h
	add al,30h
	
	; 显示
	mov bx,0b800h
	mov es,bx
	mov byte ptr es:[160*12+40*2],ah
	mov byte ptr es:[160*12+40*2+2],al
	
	mov ax,4c00h
	int 21h

code ends
end start
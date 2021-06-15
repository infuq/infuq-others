#CC = gcc
#CPPFLAGS = -I ./


%.bin:%.asm
	nasm $^ -f bin -o out/$@

objfiles = mbr.bin loader.bin
all:$(objfiles)
	dd if=out/mbr.bin of=infuq-os.img bs=512 count=1 conv=notrunc
	dd if=out/loader.bin of=infuq-os.img bs=512 count=4 seek=2  conv=notrunc

.PHONY:clean
clean:
	@$(RM) ./out/*
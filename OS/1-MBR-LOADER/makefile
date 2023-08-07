#CC = gcc
#CPPFLAGS = -I ./


%.bin:%.asm
	nasm $^ -f bin -o out/$@

infuq-os.img:
	bximage -q -hd=16M -mode=create -sectsize=512 -imgmode=flat infuq-os.img

objfiles = infuq-os.img boot.bin loader.bin
all:$(objfiles)
	dd if=out/boot.bin of=infuq-os.img bs=512 count=1 conv=notrunc
	dd if=out/loader.bin of=infuq-os.img bs=512 count=4 seek=2  conv=notrunc

run:
	bochs

.PHONY: clean
clean:
	@$(RM) ./out/*
	@$(RM) *.img *.ini


%.bin: boot/%.asm
	nasm -I boot/include/ $^ -f bin -o out/$@	

bootfiles = boot.bin loader.bin
boot.bin: $(bootfiles)


kernelfiles = kernel/main.c
kernel.bin: $(kernelfiles)
	nasm lib/kernel/print.asm -f elf -o out/print.o
	nasm kernel/kernel.asm -f elf -o out/kernel.o
	nasm thread/switch.asm -f elf -o out/switch.o
	gcc -m32 -I ./lib/ -I ./lib/kernel -I ./lib/user -c -fno-builtin -fno-stack-protector -o out/string.o lib/string.c
	gcc -m32 -I ./lib/ -I ./lib/kernel -I ./lib/user -c -fno-builtin -fno-stack-protector -o out/list.o lib/kernel/list.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/debug.o kernel/debug.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/interrupt.o kernel/interrupt.c
	gcc -m32 -I ./lib/kernel/ -I ./device -I ./thread -c -fno-builtin -fno-stack-protector -o out/init.o kernel/init.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/bitmap.o lib/kernel/bitmap.c
	gcc -m32 -I ./lib/kernel/ -c -fno-builtin -fno-stack-protector -o out/memory.o kernel/memory.c
	gcc -m32 -I ./lib/kernel/ -I ./thread -c -fno-builtin -fno-stack-protector -o out/sync.o thread/sync.c
	gcc -m32 -I ./lib/kernel/ -I ./thread -c -fno-builtin -fno-stack-protector -o out/thread.o thread/thread.c
	gcc -m32 -I ./lib/kernel/ -I ./thread -I ./device -c -fno-builtin -fno-stack-protector -o out/timer.o device/timer.c
	gcc -m32 -I ./lib/kernel/ -I ./thread -I ./device -c -fno-builtin -fno-stack-protector -o out/console.o device/console.c
	gcc -m32 -I ./lib/kernel/ -I ./thread -I ./device -c -fno-builtin -fno-stack-protector -o out/keyboard.o device/keyboard.c
	gcc -m32 -I ./lib/kernel/ -I ./thread -I ./device -I ./kernel -c -fno-builtin -fno-stack-protector -o out/ioqueue.o device/ioqueue.c
	gcc -m32 -I ./lib/kernel/ -I ./device -I ./thread -c -fno-builtin -fno-stack-protector -o out/main.o kernel/main.c

	ld -m elf_i386 -Ttext 0xc0001500 -e main -o out/kernel.bin out/main.o out/print.o out/init.o out/interrupt.o out/kernel.o out/bitmap.o out/memory.o out/string.o out/sync.o out/thread.o out/switch.o out/list.o out/timer.o out/console.o out/debug.o out/keyboard.o out/ioqueue.o


all: boot.bin kernel.bin
	dd if=out/boot.bin of=infuq-os.img bs=512 count=1 conv=notrunc
	dd if=out/loader.bin of=infuq-os.img bs=512 count=4 seek=2  conv=notrunc
	dd if=out/kernel.bin of=infuq-os.img bs=512 count=200 seek=9  conv=notrunc


.PHONY:clean
clean:
	@$(RM) ./out/*



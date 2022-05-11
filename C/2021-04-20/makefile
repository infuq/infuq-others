target=main
src=$(wildcard *.c)
objects=$(patsubst %.c,%.o,$(src))
CPPFLAGS=-I./
CC=gcc

$(target): $(objects)
	$(CC) -o $@ $^

%.o:%.c
	$(CC) -c $< $(CPPFLAGS)

.PHONY:clean
clean:
	@rm -f $(objects) $(target)

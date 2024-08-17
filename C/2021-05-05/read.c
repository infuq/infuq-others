#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char *argv)
{


	int fd = open("./myfifo", O_RDONLY);

	char buf[16];
	memset(buf, 0x00, 16);

	read(fd, buf, 6);
	printf("%s\n", buf);

	close(fd);

	return 0;

}




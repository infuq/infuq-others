#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *argv)
{

	mkfifo("./myfifo", 0777);

	int fd = open("./myfifo", O_WRONLY);
	write(fd, "xyzABC", 6);
	
	close(fd);

	return 0;

}




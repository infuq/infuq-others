#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>
#include <sys/mman.h>

void sighandler(int sig)
{

	printf("signal -> %d\n", sig);

}

int main(int argc, char *argv[])
{

	int pipefd[2];
	pipe(pipefd);

	signal(SIGPIPE, sighandler);

	close(pipefd[0]);

	write(pipefd[1],"xyzABC",6);



	return 0;

}

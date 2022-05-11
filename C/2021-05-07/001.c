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
#include <signal.h>

void sighandler(int signo)
{
	printf("signo=%d\n", signo);
}

int main(int argc, char *argv[])
{

	signal(SIGALRM, sighandler);

	int n = alarm(5);
	printf("n=%d\n", n);

	sleep(2);
	n = alarm(7);
	printf("n=%d\n", n);

//	n = alarm(0);
//	printf("n=%d\n", n);

	sleep(10);

	return 0;
}

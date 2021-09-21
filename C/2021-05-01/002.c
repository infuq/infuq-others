#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>


int main(int argc, char *argv[])
{

	struct stat statbuf;
	stat(argv[1], &statbuf);

	if (statbuf.st_mode & S_IROTH)
	{
		puts("-R-");
	}
	
	if (statbuf.st_mode & S_IWOTH)
	{
		puts("-W-");
	}
	if (statbuf.st_mode & S_IXOTH)
	{
		puts("-X-");
	}


	return 0;

}

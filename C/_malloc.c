#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>



int main(int argc, const char *argv[])
{
	

	int * ptr = (int *)malloc(1024);
	printf("%p\n", ptr);

	return 0;

}

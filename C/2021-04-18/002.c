#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>


int main(int argc, const char *argv[])
{

	printf("%d\n", argc);
	int i = 0;
	while (i < argc)
	{
		printf("%s ", argv[i]);
		i += 1;
	}
	printf("\n");

	return 0;

}

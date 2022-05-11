#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>

#include "add.h"
#include "sub.h"

int main(int argc, char *argv[])
{

	add();
	sub();

	return 0;

}

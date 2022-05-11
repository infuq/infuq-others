#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>
#include <dirent.h>

int main(int argc, char *argv[])
{

	DIR *pDir = opendir(argv[1]);
	if (pDir == NULL)
	{
		perror("opendir error");
		return -1;
	}

	struct dirent *pDent = NULL;
	while ( (pDent = readdir(pDir)) != NULL )
	{

		if ( strcmp(pDent->d_name, ".") == 0 
				|| 
			 strcmp(pDent->d_name, "..") == 0
			)
		{
			continue;
		}

		printf("%s\t ",pDent->d_name);
		switch (pDent->d_type)
		{
		case DT_REG:
			puts("Regular File");
			break;
		case DT_DIR:
			puts("Dir");
			break;
		case DT_LNK:
			puts("LINK");
			break;
		default:
			puts("UNKNOWN");
			break;
		}

	}



	return 0;

}



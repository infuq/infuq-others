#include <stdio.h>
#include <dirent.h>

int main(void)
{
	DIR		*dirptr = NULL;
	struct dirent	*entry;
	if ((dirptr = opendir(".")) == NULL)
	{
		printf("opendir failed!");
		return(1);
	}
    
	while (entry = readdir(dirptr))
	{
	    printf("file_name=%s\n", entry->d_name);
	}
	closedir(dirptr);
	
	return(0);
}

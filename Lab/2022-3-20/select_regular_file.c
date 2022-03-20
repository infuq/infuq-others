#include <stdio.h>
#include <sys/select.h>
#include <sys/types.h>    
#include <sys/stat.h>    
#include <fcntl.h>
#include <unistd.h>

int main()
{

    int max = 10;
    int fd;
    fd = open("/Users/infuq/tmp/server.c", O_RDWR); 

    fd_set rset;
    fd_set wset;

    FD_ZERO(&rset);
//    FD_SET(fd, &rset);
    FD_SET(fd, &wset);

    int maxfd = fd;

    while (max--)
    {
        select(maxfd+1, &rset, &wset, NULL, NULL);
     
        if (FD_ISSET(fd, &rset))
        {
            printf("read -> %d\n", fd);
        }
    
        if (FD_ISSET(fd, &wset))
        {
            printf("write -> %d\n", fd);
        }

    }

    close(fd);

    return 0;
}

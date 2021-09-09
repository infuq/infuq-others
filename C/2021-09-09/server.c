#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <errno.h>
#include <stddef.h>
#include <unistd.h>

#define MAX_CONNECT_NUM 2
#define BUFFER_SIZE 1024

const char *filename = "unix.domain.socket";

int main(int argc, char **argv)
{
    int         lfd, fd, len, i;
    struct sockaddr_un  un;

    lfd = socket(AF_UNIX, SOCK_STREAM, 0);
    if (lfd < 0)
    {
        printf("Create socket fail.\n");
        return -1;
    }
    un.sun_family = AF_UNIX;
    unlink(filename);
    strcpy(un.sun_path, filename);

    if ( bind(lfd, (struct sockaddr *) &un, sizeof(un)) < 0 )
    {
        printf("bind fail...\n");
        return -1;
    }
    if ( listen(lfd, MAX_CONNECT_NUM) < 0 )
    {
        printf("listen fail...\n");
        return -1;
    }
    while (1)
    {
        struct sockaddr_un  client_addr;
        char            buffer[BUFFER_SIZE];
        bzero(buffer, BUFFER_SIZE);
        len = sizeof(client_addr);
        printf("accepting...\n");
        /* fd = accept(fd, (struct sockaddr *)&client_addr, &len); */
        fd = accept(lfd, NULL, NULL);
        if (fd < 0)
        {
            printf("accept fail...\n");
            return -1;
        }
/*
        int ret = recv(fd, buffer, BUFFER_SIZE, 0);
        if (ret < 0)
        {
            printf("recv fail...\n");
        }
        for (i = 0; i < 10; i++)
        {
            printf(" %d", buffer[i]);
        }

  */    
        printf("\n");
//        close(fd);
        //break;
    }
    close(lfd);

    return 0;

}




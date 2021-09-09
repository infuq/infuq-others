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

#define BUFFER_SIZE 1024
const char *filename = "unix.domain.socket";

int main(int argc, char **argv)
{
    struct sockaddr_un  un;
    int             fd;
    char            buffer[BUFFER_SIZE] = { 1, 2, 3 };
    un.sun_family = AF_UNIX;

    strcpy(un.sun_path, filename);
    fd = socket(AF_UNIX, SOCK_STREAM, 0);
    if (fd < 0)
    {
        printf("Create socket fail...\n" );
        return -1;
    }
    if (connect(fd, (struct sockaddr *) &un, sizeof(un)) < 0 )
    {
        printf("connect socket fail...\n" );
        return -1;
    }
    printf("send data...\n");
    send(fd, buffer, BUFFER_SIZE, 0);

    close(fd);

    return 0;

}




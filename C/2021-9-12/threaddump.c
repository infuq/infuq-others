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

#define BUFFER_SIZE 8192
const char *filename = "/tmp/.java_pid6617";

int main(int argc, char **argv)
{
        struct sockaddr_un  un;
        int             fd;
        char            buffer[BUFFER_SIZE];
        char            *cmd = "1\0threaddump\0\0\0\0"; // 长度16
        
        un.sun_family = AF_UNIX;
        strcpy(un.sun_path, filename);

        fd = socket(PF_UNIX, SOCK_STREAM, 0);
        connect(fd, (struct sockaddr *) &un, sizeof(un));

        // 方式一 
        send(fd, cmd, 16, 0);
        recv(fd, buffer, BUFFER_SIZE, 0);
        
        // 方式二
        //write(fd, cmd, 16);
        //read(fd, buffer, BUFFER_SIZE);


        printf("\n%s\n", buffer);

        close(fd);

        return 0;

}

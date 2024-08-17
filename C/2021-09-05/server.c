#include <stdio.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <errno.h>
#include <arpa/inet.h>


int main()
{

    fd_set rset;
    int maxfd = -1;

    struct timeval time;

    lfd = socket(...);
    
    bind(lfd,);

    listen(lfd);

    FD_ZERO(&rset);
    FD_SET(lfd, &rset)
#if 0
    select(maxfd+1, &rset, NULL, NULL, NULL);
#else
    time.tv_sec = 5;
    time.tv_usec = 0;
    select(maxfd+1, &rset, NULL, NULL, NULL);
#endif

    if (FD_ISSET(lfd, &rset))
    {
        int newfd = accept(lfd);   
    }
    


    return 0;
}

#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>

/*
usage: ./a.out www.infuq.com
*/
int main(int argc, char **argv)
{

    struct hostent *hp = NULL;
    if ( (hp = gethostbyname(argv[1])) == NULL )
    {
        herror("gethostbyname error");
        exit(1);
    }

    int i = 0;
    while ( hp->h_addr_list[i] != NULL )
    {
        printf("hostname: %s\n", hp->h_name);
        printf("      ip: %s\n", inet_ntoa( *(struct in_addr *) hp->h_addr_list[i] ) );   
        i++;
    }

    endhostent();
    hp = NULL;

    return 0;

}

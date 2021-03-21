#include<stdio.h>


int main()
{

    int a = 0x02000001;

    char *ptr = (char *) &a;
    printf("%d\n", *ptr);// =1   小端存储

    printf("%d\n", *(ptr+3));// =2


    return 0;
}
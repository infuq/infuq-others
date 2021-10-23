#include <stdio.h>

union Un
{
    char i;
    int year;
};

int main(int argc, char **argv)
{

    union Un un;

    printf("%ld\n", sizeof(un));

    printf("%p\n", &un);
    printf("%p\n", &(un.i));
    printf("%p\n", &(un.year));

    return 0;
}
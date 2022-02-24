#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void count(int arr[])
{
    printf("size=%ld\n", sizeof(arr)); // 8
}

int main(int argc, char **argv)
{

    int arr[] = {1, 2, 5, 7};
    printf("size=%ld\n", sizeof(arr)); // 16

    count(arr);

    int *ptr = NULL;
    printf("size=%ld\n", sizeof(ptr)); // 8

}


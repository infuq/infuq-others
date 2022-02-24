#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void count(int arr[])
{
    // 不论arr的容量是多少,sizeof(arr)始终等于sizeof(int *)
    printf("size=%ld\n", sizeof(arr)); // 8字节
}

int main(int argc, char **argv)
{

    int arr[] = {1, 2, 5, 7};
    printf("size=%ld\n", sizeof(arr)); // 16字节

    count(arr);

    int *ptr = NULL;
    printf("size=%ld\n", sizeof(ptr)); // 8字节

}


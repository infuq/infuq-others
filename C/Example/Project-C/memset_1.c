#include<stdio.h>
#include<string.h>


void memset_1()
{
    char content[] = "this is a test";
    printf("%s\n", content);

    memset(content, '-', 4);
    printf("%s\n", content);



}

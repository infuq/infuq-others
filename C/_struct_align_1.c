#include<stdio.h>

/*
结构体内存对齐
*/

struct Stu
{
    char c;
    int year;
    char k;
};


struct Tch
{
    char k;
    char c;
    int year;
};

void _struct_align_1()
{

    printf("%lu\n", sizeof(struct Stu));//12

    printf("%lu\n", sizeof(struct Tch));//8


}
#include<stdio.h>


struct Stu//24
{
    char c;
    double time;
    int year;
    char k;
};
struct Tch//40
{
    char c;
    int year;
    struct Stu stu;
    double time;
};


struct Tch2//24
{
    char c;
    int year;
    struct Stu* stu;//8
    double time;
};

void struct_align_2()
{

    printf("%d\n", sizeof(struct Stu));
    printf("%d\n", sizeof(struct Tch));
    printf("%d\n", sizeof(struct Tch2));


}
#include<stdio.h>


struct Stu
{
    int year;
    char sex;
    double time;
    char name[20];
};

void _struct_4()
{
    struct Stu stu = { 2021, '1', 5435423.5, "Libai" };

    printf("%d %c %lf %s\n", stu.year, stu.sex, stu.time, stu.name);

}




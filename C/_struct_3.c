#include<stdio.h>


struct
{
    int a;
    char c;
} stu;

struct
{
    int a;
    char c;
}  *ptr, stu2;


void _struct_3()
{

    // ptr = &stu;  Error
    ptr = &stu2;

}



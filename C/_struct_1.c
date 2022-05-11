#include<stdio.h>

typedef struct stu
{
    struct stu* next;
    // Stu *next;   // Error
    // struct stu next; // Error
    int age;
} Stu;

void _struct_1()
{
    struct stu stu1;
    Stu stu2;

    stu1.age = 12;
    stu2.age = 16;

    printf("%d\n", stu1.age);
    printf("%d\n", stu2.age);

}


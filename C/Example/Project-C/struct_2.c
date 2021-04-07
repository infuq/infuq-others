#include<stdio.h>

/*
结构体作为地址

*/


typedef struct stu
{
    int age;
    char name[20];
} Stu;

void printInfo(Stu* ptr)
{
    printf("%d %s\n", ptr->age, ptr->name);
    // 可以修改结构体中的值
    ptr->age = 10;
}

void printInfo2(const Stu* ptr)
{
    printf("%d %s\n", ptr->age, ptr->name);
    // 不可以修改结构体中的值
    // ptr->age = 10;   // Error
}

void struct_2()
{

    Stu stu = { 20, "Libai" };
    printf("%d\n", stu.age);

    printInfo(&stu);
    printf("%d\n", stu.age);


}


#include <stdio.h>

void print(int (*ptr)[5], int r, int c)
{

    for (int i = 0; i < r; i++)
    {
        printf("%d ", *(*(ptr + i)));
        for (int j = 0; j < c; j++)
        {
            
            printf("%d ", *(*(ptr + i) + j));

        }
        printf("\n");
    }
}


int main()
{

    int arr[] = { 1,2,3,4,5 };

    // 虽然也可以这么写,但严格讲,不正确. 正确写法: int *ptr = arr; 或者 int (*ptr)[5] = &arr;
    /*
    int (*ptr)[5] = arr;
    printf("%p\n", ptr);
    printf("%p\n\n", ptr + 1);
*/

    int (*ptr2)[5] = &arr;// 正确
    printf("%p\n", ptr2);
    printf("%p\n", ptr2 + 1);

    int arr2[3][5] = {{1,2,3,4,5},{2,3,4,5,6},{3,4,5,6,7}};
    print(arr2, 3, 5);

    int arr3[] = {1,2,3,4,5,6,7};
    int *ptr3 = arr3;
    printf("%d ", *(ptr3 + 1));
    printf("%d\n", *(ptr3 + 2));
    int (*ptr4)[7] = &arr3;

    printf("%p\n", ptr4);
    printf("%p\n", *(ptr4 + 0));
    int v = *(*(ptr4 + 0) + 3);
    printf("%d\n", v);

    return 0;
}
/*
输出结果

0x7ffff4a8d720
0x7ffff4a8d734

0x7ffff4a8d720
0x7ffff4a8d734

*/

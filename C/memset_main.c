#include<stdio.h>
#include<string.h>


int main()
{
    char content[] = "this is a test";
    printf("%s\n", content);

    memset(content, '-', 4);
    printf("%s\n", content);

    return 0;
        
}
 
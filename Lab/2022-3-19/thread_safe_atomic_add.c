#include <stdio.h>
#include <pthread.h>

// gcc -pthread thread_safe_atomic_add.c

long sum = 0;

void * _sum(void *arg)
{
    for (int i = 0; i < 100000000; i++)
    {
        //__asm__ volatile("addq $1, %0": "+m"(sum));
        __asm__ volatile("lock addq $1, %0": "+m"(sum));
    }

    return NULL;
}


int main()
{

    pthread_t t1;
    pthread_t t2;

    pthread_create(&t1, NULL, _sum, NULL);
    pthread_create(&t2, NULL, _sum, NULL);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("sum = %ld\n", sum);

    return 0;

}

#include <stdio.h>
#include <pthread.h>

// gcc -pthread thread_safe_atomic_xchg.c
// gcc -std=c99 -pthread thread_safe_atomic_xchg.c

int index = 9527;

void * _xchg(void *arg)
{
    int *new_val = (int *)arg;

    int rt;
    __asm__ volatile("lock xchg %0, %1": "+m"(index), "=a"(rt): "1"(*new_val));

    printf("=> %d\n", rt);
    return NULL;
}


int main()
{

    int i = 9528;
    int j = 9529;
    pthread_t t1;
    pthread_t t2;
    pthread_create(&t1, NULL, _xchg, &i);
    pthread_create(&t2, NULL, _xchg, &j);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    return 0;

}

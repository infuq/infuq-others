#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *add(void *arg)
{
    pthread_mutex_lock(&mutex);
    while (1)
    {
        printf("%d\n", 1);
    }
    pthread_mutex_unlock(&mutex);

}
void *sum(void *arg)
{
    pthread_mutex_lock(&mutex);
    sleep(3600);
    pthread_mutex_unlock(&mutex);
}

int i =1;

int main()
{
    
    pthread_t add_thread;
    pthread_t sum_thread;

    pthread_create(&add_thread, NULL, add, NULL);
    pthread_create(&sum_thread, NULL, sum, NULL);

    pthread_join(add_thread, NULL);

    return 0;
}

/*

[v-infuq: ~]# ps -Lf 337
UID        PID    PPID     LWP    C    NLWP         STIME      TTY      STAT       TIME     CMD
v-infuq    337     9       337    0    3            22:17      tty1     Sl         0:00     ./pthread_2022_2_3
v-infuq    337     9       338    23   3            22:17      tty1     Rl         0:15     ./pthread_2022_2_3
v-infuq    337     9       339    0    3            22:17      tty1     Sl         0:00     ./pthread_2022_2_3



 */




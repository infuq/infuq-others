#! /usr/bin/env python

"""
线程池
"""

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import time
import threading
import random


def invoke(t):
    time.sleep(t)
    print("{} invoke success".format(threading.currentThread().getName()))  # My_0 invoke success
    return t + 3


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=8, thread_name_prefix='My')
    times = [random.randint(1, 7) for _ in range(5)]

    tasks = [executor.submit(invoke, time) for time in times]
    # 等待任务满足某个条件才继续
    wait(tasks, return_when=FIRST_COMPLETED)

    # 方式一
    # 谁先完成就会先获取到它的结果
    for future in as_completed(tasks):
        data = future.result()
        print(data)

    # 方式二
    # 返回结果的顺序与times中的值的顺序一致
    for data in executor.map(invoke, times):
        print(data)

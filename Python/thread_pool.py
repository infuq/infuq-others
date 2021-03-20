#! /usr/bin/env python

from concurrent.futures import ThreadPoolExecutor
import time
import threading

def invoke(times):
    time.sleep(times)
    print("{} invoke success".format(threading.currentThread().getName()))# My_0 invoke success
    return times + 3


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=8, thread_name_prefix='My')
    task = executor.submit(invoke, (3))
    print(task.done())# False
    time.sleep(4)
    print(task.done())# True

    # 取消某个任务
    print(task.cancel())# False 表示取消失败 可能已经在运行或者运行完成

    # 阻塞获取结果
    print(task.result())# 6


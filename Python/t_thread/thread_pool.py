#! /usr/bin/env python

"""
线程池
"""

from concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests
import time


def invoke(times):
    # time.sleep(times)
    # print("{} invoke success".format(threading.currentThread().getName()))  # My_0 invoke success

    response = requests.get('http://localhost:58081/local/doSleep')

    return times + 3


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=30, thread_name_prefix='My')

    while True:
        time.sleep(2)
        # 这个返回值task很重要.   submit方法非阻塞
        task = executor.submit(invoke, (3))
        
        # 判断任务是否完成
        print(task.done())  # False
        # time.sleep(4)
        # print(task.done())  # True

        # # 取消某个任务
        # print(task.cancel())  # False 表示取消失败 可能已经在运行或者运行完成

        # # 阻塞获取结果
        # print(task.result())


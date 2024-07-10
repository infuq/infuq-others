#! /usr/bin/env python

import asyncio
import threading
import time
import dis
import inspect

async def mock():
    print('2', threading.current_thread().name)
    await asyncio.sleep(3) # 向 EventLoop 中的 _scheduled 添加一个任务

    # 执行完成之后, 会向 _ready 中添加一个任务(Task.task_wakeup)
    return "模拟"


async def main():
    print('1', threading.current_thread().name)
    task = asyncio.create_task(mock()) # 向 EventLoop 中的_ready 添加一个任务

    ret = await task
    print('main#', ret)


if __name__ == '__main__':

    asyncio.run(main())


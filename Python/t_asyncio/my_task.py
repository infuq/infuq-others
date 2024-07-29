#! /usr/bin/env python

import asyncio
import threading
import time
import dis


async def mock():
    print('2', threading.current_thread().name)
    await asyncio.sleep(3) # 向 EventLoop 中的 _scheduled 添加一个任务

    # 执行完成之后, 会向 _ready 中添加一个任务(Task.task_wakeup)
    return "模拟"


def _task_finish_cb(ret):
    print('3', threading.current_thread().name)
    print('_task_finish_cb', ret)


async def main():
    print('1', threading.current_thread().name)
    task = asyncio.create_task(mock()) # 向 EventLoop 中的_ready 添加一个任务
    task.add_done_callback(_task_finish_cb)
    ret = await task
    print('main#', ret)


if __name__ == '__main__':
    # 底层会添加一个回调 _run_until_complete_cb , 回调内部会停止事件循环 self._stopping = True
    asyncio.run(main())


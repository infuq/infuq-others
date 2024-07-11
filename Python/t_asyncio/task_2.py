#! /usr/bin/env python

import asyncio
import threading
import time
import dis
import inspect
from objprint import op


async def mock():
    print('2', threading.current_thread().name)

    return "模拟"


def _task_finish_cb(ret):
    print('3', threading.current_thread().name)
    print('_task_finish_cb', ret)
    frame = inspect.currentframe()
    op(
        frame,
        honor_existing=False,
        depth=2
    )


async def main():
    print('1', threading.current_thread().name)
    task = asyncio.create_task(mock())
    task.add_done_callback(_task_finish_cb)

    ret = await task
    print('main#', ret)


if __name__ == '__main__':

    asyncio.run(main())


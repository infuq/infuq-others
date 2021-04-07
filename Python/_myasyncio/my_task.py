#! /usr/bin/env python

import asyncio
import threading
import time


async def mock():
    print("---1---", threading.currentThread().getName())
    await asyncio.sleep(3)
    print("---2---", threading.currentThread().getName())
    return "模拟"


async def main():
    print("---3---", threading.currentThread().getName())
    task = asyncio.create_task(mock())
    print("---4---", threading.currentThread().getName())
    ret = await task


if __name__ == '__main__':
    print("---5---", threading.currentThread().getName())
    asyncio.run(main())
    print("---6---", threading.currentThread().getName())
    time.sleep(6)
    print("---7---", threading.currentThread().getName())



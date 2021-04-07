#! /usr/bin/env python

import asyncio
import threading
import time


async def mock():
    await asyncio.sleep(3)
    return "模拟"


async def main():
    task = asyncio.create_task(mock())
    ret = await task


if __name__ == '__main__':
    asyncio.run(main())

    asyncio.new_event_loop()



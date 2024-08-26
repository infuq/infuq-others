#! /usr/bin/env python

import asyncio


async def coro():
    print("something is running")

def done_finish(task):
    print('callback ...', task)

async def main():
    task = asyncio.create_task(coro())
    task.add_done_callback(done_finish)
    loop = asyncio.get_running_loop()
    print(loop)
    loop = asyncio.get_event_loop()
    print(loop)

if __name__ == '__main__':
    asyncio.run(main(), debug=True)



#! /usr/bin/env python

import asyncio


async def run():
    print('run...')
    await asyncio.sleep(3)


if __name__ == '__main__':
    print('start...')

    loop = asyncio.get_event_loop()
    loop.create_future()

    print('end...')

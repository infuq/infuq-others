#! /usr/bin/env python3

import asyncio

async def read_file(file_path):
    async with asyncio.StreamReader(file_path, 'r') as file:
        data = await file.read()
        print(data)

if __name__ == '__main__':
    asyncio.run(read_file('example.txt'))

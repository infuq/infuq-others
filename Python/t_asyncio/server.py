#! /usr/bin/env python3

import asyncio

async def handle_client(reader, writer):
    # 从客户端读取数据
    data = await reader.read(1024)
    message = data.decode()
    # 获取客户端地址
    addr = writer.get_extra_info('peername')
    print(f"Received {message!r} from {addr!r}")
    # 将收到的数据发送回客户端
    writer.write(data)
    # 强制数据发送并清空缓冲区
    await writer.drain()
    print(f"Send: {message!r}")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8080)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())


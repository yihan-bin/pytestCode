import asyncio
import time

class AsyManager:
    def __init__(self):
        self.conn = conn

    async def do_something(self):
        return 666

    async def __aenter__(self):
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(1)

async def func():
    async with AsyManager() as f:
        result = await f.do_something()
        print(result)
        print(time.time()-start)

start=time.time()
asyncio.run( asyncio.wait(func()))
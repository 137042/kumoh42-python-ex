import asyncio
import aiohttp
import time


URL = 'https://httpbin.org/uuid'


async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])


async def main():
    async with aiohttp.ClientSession(connector =aiohttp.TCPConnector(verify_ssl= False)) as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    duration = time.time() - start_time
    print(f"{duration} seconds")
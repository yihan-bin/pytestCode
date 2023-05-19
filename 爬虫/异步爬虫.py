import aiohttp
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}
async def Fetch(session,url):
    print('发送请求：',url)
    async with session.get(url) as respose:
        text = await respose.text()
        print('得到结果：',url,len(text))


async def main():
    async with aiohttp.ClientSession() as session:
        url_List=[
            'https://www.baidu.com',
            'https://www.sougou.com',
            'https://www.pythonav.com',
        ]
        tasks = [asyncio.create_task(Fetch(session,url)) for url in url_List]
        done,pending = await asyncio.wait(tasks)




if __name__ == '__main__':
    asyncio.run(main())
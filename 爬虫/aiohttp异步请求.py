# import requests
# import asyncio
# import time
# start=time.time()
# urls = ['Http://127.0.0.1:5000/bobo','Http://127.0.0.1:5000/jay','Http://127.0.0.1:5000/tom']
# async def get_page(url):
#     print('正在下载{}'.format(url))
#     respose = requests.get(url = url)#requests是基于同步的网络请求，不能用于异步请求里面
#     print('下载完毕',respose.text)
# tasks = []
# for url in urls:
#     c=get_page(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# print(time.time()-start)
#
# print('zjabd')



import requests
import asyncio
import time
import aiohttp
start=time.time()
urls = ['Http://127.0.0.1:5000/bobo','Http://127.0.0.1:5000/jay','Http://127.0.0.1:5000/tom']
async def get_page(url):
    print('正在下载{}'.format(url))
    async with aiohttp.ClientSession() as session:
        #get().post():
        #headers
        #get()里面使用par ams,post()里面使用的 桉树data
        #代理IP处理，Proxy='http:/IP:port'
        async with session.get(url) as response:
            #.text返回的是字符串形式的响应数据
            #.read()返回的二进制形式的响应数据
            #.jaso()返回的是json对象
            page_Text = response.text()
            print(page_Text)

    print('下载完毕', page_Text)
tasks = []
for url in urls:
    c=get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start)


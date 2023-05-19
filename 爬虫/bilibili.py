import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

}
url = 'https://www.bilibili.com/ranking'

respone = requests.get(url, headers=headers)
html_text = respone.text

soup = BeautifulSoup(html_text,'html.parser')

items = soup.findAll('li',{'class':'rank-item'})#定位标签

print(len(items))
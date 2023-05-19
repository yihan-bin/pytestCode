import requests
from lxml import etree
a = 10
for i in range(5):
    print(i)
dic = {'name': '张三', 'age': '20',  'birth': '1993/3/3'}
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

    }

    url = 'https://bj.58.com/ershoufang/?PGTID=0d100000-0000-11f5-999b-6033e523af0b&ClickID=2'
    house_info = requests.get(url=url, headers=headers).text
    tree = etree.HTML(house_info)

    div_list = tree.xpath('//section[@class="list"]/div')
    for div in div_list:
        title = div.xpath('./a/div[2]/div[1]//div[1]/p[5]/text()')[0]
        with open('./58title.txt', 'a', encoding='utf-8') as fp:
            fp.write(title + '\n')
            print(title,end='\t')





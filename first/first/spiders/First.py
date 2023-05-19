import scrapy


# class FirstSpider(scrapy.Spider):
#     name = 'First'
#  #   allowed_domains = ['www.xxx.com']
#     start_urls = ['https://www.qiushibaike.com/text/']
#
#     def parse(self, response):
#         all_data = []
#         div_list = response.xpath('//div[@id="content"]/div/div[2]')
#         for div in div_list:
#
#
#             author = div.xpath('./div/div[1]/a[2]/h2/text()')[0].extract()
#             content = div.xpath('./div/a/div/span/text()').extract()
#             content = ''.join(content)
#             print(author,content)
#             dic = {
#                 'author': author,
#                 'content':content
#             }
#             all_data.append(dic)
#         return  all_data
#     #持久化存储第一种  scrapy crawl SpiderName -o FileName,其格式只能为('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')



from first.items import FirstItem
class FirstSpider(scrapy.Spider):
    name = 'First'
 #   allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="content"]/div/div[2]')
        for div in div_list:


            author = div.xpath('./div/div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./div/a/div/span/text()').extract()
            content = ''.join(content)

            item = FirstItem()
            item['author'] = author
            item['content'] = content

            yield item


import scrapy
from scrapy import Selector
from ..items import FirstproItem

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.douban.com']
    url='https://www.douban.com/doulist/152361157/?start='
    str='&sort=time&playable=0&sub_type='


    start_urls ='https://www.douban.com/doulist/152361157/?start=0&sort=time&playable=0&sub_type='

    def parse(self, response):
        items=FirstproItem()
        list_items=response.css('#content > div > div.article>div')
        for list_item in list_items:
            items['title']=list_item.css('div > div.bd.doulist-subject > div.title::text')
            items['rating']=list_item.css('div > div.bd.doulist-subject > div.rating::text')





            for i in range(1, 11):
                trans = F'{i * 25}'
                concat ='https://www.douban.com/doulist/152361157/?start=' + trans +'&sort=time&playable=0&sub_type='
                yield scrapy.Request(url=concat,callback=self.parse())
                #爬取多个页面，使用callback回调函数
        pass

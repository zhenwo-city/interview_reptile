import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['iftp.chinamoney.com.cn']
    start_urls = ['http://iftp.chinamoney.com.cn/english/bdInfo/']

    def parse(self, response):
        # for each in range(1,16):
            isin =
            bond_code = scrapy.Field()
            issuer = scrapy.Field()
            bond_type = scrapy.Field()
            issue_date = scrapy.Field()
            latest_rating = scrapy.Field()
        pass
//*[@id="sheet-bond-market"]/div[1]/div/table/tbody/tr[1]/td[1]
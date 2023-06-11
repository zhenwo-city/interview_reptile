# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    rating=scrapy.Field()
    src=scrapy.Field()
    writer=scrapy.Field()
    press=scrapy.Field()
    press_time=scrapy.Field()
    pass

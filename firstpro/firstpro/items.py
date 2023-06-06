# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    isin=scrapy.Field()
    bond_code=scrapy.Field()
    issuer=scrapy.Field()
    bond_type=scrapy.Field()
    issue_date=scrapy.Field()
    latest_rating=scrapy.Field()
    pass

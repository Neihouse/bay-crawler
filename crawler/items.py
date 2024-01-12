import scrapy

class EmailItem(scrapy.Item):
    email = scrapy.Field()
    source_url = scrapy.Field()
import scrapy

class EventProductionItem(scrapy.Item):
    email = scrapy.Field()
    source_url = scrapy.Field()
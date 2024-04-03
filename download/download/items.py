# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class DownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files  = scrapy.Field()
    filename = scrapy.Field(output_processor = TakeFirst())
    

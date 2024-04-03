import scrapy
from scrapy.loader import ItemLoader
from download.items import DownloadItem

class PdfSpider(scrapy.Spider):
    name = "pdf"
    #allowed_domains = ["www.bitsavers.org"]
    start_urls = ["http://www.bitsavers.org/pdf/sony/floppy"]

    def parse(self, response):
        for article in response.xpath("//a[contains(@href, '.pdf')]"):
            loader = ItemLoader(item=DownloadItem(), selector=article)
            relative_url = article.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            loader.add_xpath('filename', ".//text()")
            yield loader.load_item()


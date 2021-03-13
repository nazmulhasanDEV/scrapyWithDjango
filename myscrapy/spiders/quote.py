import scrapy
from myapp.models import Data
from myscrapy.items import MyscrapyItem

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath("//div[@class='quote']/span[@class='text']")
        for x in quotes:
            item = MyscrapyItem()
            title = x.xpath(".//text()").get()
            item['title'] = title
            yield item

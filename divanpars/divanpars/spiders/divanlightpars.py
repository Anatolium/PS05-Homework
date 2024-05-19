import scrapy


class DivanlightparsSpider(scrapy.Spider):
    name = "divanlightpars"
    allowed_domains = ["https://www.divan.ru"]
    # start_urls - это та ссылка, от которой начинается парсинг
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href']
            }

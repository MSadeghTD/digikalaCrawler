import scrapy


class ProductSpider(scrapy.Spider):
    name = "products"
    # download_delay = 1

    def start_requests(self):
        urls = [
            'https://www.digikala.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'digikala.html'

        # r = response.css('.productItem').extract()
        # print("------------------------------------------------------------------------------------------")
        # print(r)
        # print("------------------------------------------------------------------------------------------")

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


import scrapy
import xlwt

class ProductSpider(scrapy.Spider):
    name = "baneKalaProducts"

    def start_requests(self):
        urls = [
            'https://banekala.ir/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        r = response.css(".item-box.effect-bubba")
        book = xlwt.Workbook(encoding="utf-8")
        sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
        sheet1.write(0, 0, "name")
        sheet1.write(0, 1, "img-link")
        sheet1.write(0, 2, "price")
        sheet1.write(0, 3, "old-price")
        row = 1
        for item in r:
            name = item.css(".type::text").extract_first()
            link = "https://banekala.ir" + item.css("div .productImage::attr(src)").extract_first()
            oldPrice = item.css(".pirces .price1-1::text").extract_first()
            price = item.css(".pirces .price1-2::text").extract_first()
            sheet1.write(row, 0, name)
            sheet1.write(row, 1, link)
            sheet1.write(row, 2, price)
            sheet1.write(row, 3, oldPrice)
            row += 1

        book.save("BaneKalaData.xls")


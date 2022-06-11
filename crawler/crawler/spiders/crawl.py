import scrapy


class Crawler(scrapy.Spider):
    name = "crawler"

    def start_requests(self):
        # Put your crawling url here
        # Can put multiple urls
        urls = [
            'https://databricks.com/dataaisummit/2022-sponsors',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # to figure out the proper xpath
        # use `scrapy shell your_url` to explore the xpath
        for data in response.xpath('//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href').getall():
            yield {
                'data': data
            }

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'databricks'
    start_urls = [
        'https://databricks.com/dataaisummit/2022-sponsors',
    ]

    def parse(self, response):
        # import pdb
        # pdb.set_trace()

        for name in response.xpath('//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href').getall():
            yield {
                'sponsor_website': name
            }

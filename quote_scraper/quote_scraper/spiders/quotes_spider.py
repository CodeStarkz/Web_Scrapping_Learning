import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # explore the respose object
        print("response:", response)
        print("response_status:", response.status)
        print("Response headers:", response.headers)
        # view page content
        print("response_text:", response.text[:200])
        # page title
        print("page title:", response.css('title::text').get())


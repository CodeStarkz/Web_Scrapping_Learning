import scrapy


class SpiderQQSpider(scrapy.Spider):
    name = "spider_q_q"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        element_container = response.css('div.quote')

        for item in element_container:
            yield {
                "Author": item.css('small.author::text').get(),
                "Quote": item.css('span.text::text').get(),
                "Tags": item.css('div.tags a.tag::text').getall()
            }
        # navigate to next link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        else:
            return("No more quotes")


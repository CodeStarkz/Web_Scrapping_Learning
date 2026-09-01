import scrapy


class ScrapiaSpider(scrapy.Spider):
    name = "scrapia"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quote = response.css("div.quote")
        nextLine = response.css("li.next a::attr(href)").get()
        for i in quote:
            yield {"Quote": i.css("span.text::text").get(),
                   "Author": i.css("small.author::text").get(),
                   "Tags": i.css("div.tags a.tag::text").getall()
                   }
            nextLine = response.css("li.next a::attr(href)").get()
            # next page handling
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page,callback=self.parse)

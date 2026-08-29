import scrapy


class CustomexpSpiderSpider(scrapy.Spider):
    name = "customexp_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    # Corrected and valid custom configurations
    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS": 2,
        "FEEDS": {
            "quotes_output.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 4,
            }
        },
        "LOG_LEVEL": "INFO",
        "LOG_STDOUT": True,
        "RETRY_TIMES": 2,  # Fixed: Replaced invalid LOG_RETRIES
    }

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            yield {
                # Extracts the author
                "author": quote.css('small.author::text').get(),

                # Quotes
                "Quotes": quote.css('span.text::text').get(),

                # Tags
                "Tags": quote.css('div.tags a.tag::text').getall(),
            }

        # Pagination handling
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


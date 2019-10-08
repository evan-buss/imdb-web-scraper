import scrapy


class BenchmarkSpider(scrapy.Spider):
    name = 'benchmark'

    ustom_settings = {
        'ITEM_PIPELINES': {
            'scraper.pipelines.MovieToDBPipeLine': 300
        },
        'ROBOTSTXT_OBEY': False,
        # 'DEPTH_LIMIT': 5,
        'CONCURRENT_REQUESTS': 16
    }

    start_urls = ['https://evanbuss.com']

    def parse(self, response):
        yield {
            'url': response.url
        }

        # Return an array of all recommended movie links
        new_links = response.css('a::attr(href)').getall()

        # Performs a depth first traversal.
        for link in new_links:
            yield response.follow(link, callback=self.parse)

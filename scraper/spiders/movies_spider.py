# This spider will extract movies from IMDB

import scrapy
import unicodedata
import sqlite3


class MoviesSpider(scrapy.Spider):
    name = 'movies'

    # start_urls = ['https://www.imdb.com/title/tt0944947/']
    start_urls = ['https://www.imdb.com/title/tt0808146/']

    def parse(self, response):
        yield {
            'title': str.strip(unicodedata.normalize('NFKD', response.css('div.title_wrapper h1::text').get())),
            'year': response.css('span#titleYear a::text').get(),
            'rating': response.css('div.ratingValue strong span::text').get()
        }

        # Return an array of all recommended movie links
        new_links = response.css('div.rec_item a::attr(href)').getall()

        # Basically performs a depth first search following each link
        for link in new_links:
            yield response.follow(link, callback=self.parse)

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    author = scrapy.Field()

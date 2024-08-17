import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from t_scrapy_example.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        for page in range(10):
            yield Request(
                url=f'https://movie.douban.com/top250?start={page*25}&filter=',
                meta={'proxy': ''}
            )

    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response:HtmlResponse, **kwargs):
        sel = Selector(response)
        item_lists = sel.css('#screening > div.screening-bd > ul > li')
        for item_list in item_lists:
            movie = MovieItem()
            movie['title'] = item_list.css('li.title > a::text').extract_first()
            movie['rating'] = item_list.css('span.subject-rate::text').extract_first()

            param_dict = {
                'item': movie
            }

            # 解析页面中的超链接并组装成Request,交给引擎
            detail_url = ''
            yield Request(
                url=detail_url,
                callback=self.parse_detail,
                cb_kwargs=param_dict
            )

    def parse_detail(self, response, **kwargs):
        movie = kwargs['item']
        movie['author'] = ''
        yield movie


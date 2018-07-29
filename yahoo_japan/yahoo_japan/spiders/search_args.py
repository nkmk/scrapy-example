# -*- coding: utf-8 -*-
import scrapy


class SearchArgsSpider(scrapy.Spider):
    name = 'search_args'
    allowed_domains = ['yahoo.co.jp']

    def __init__(self, query='', rank=0, *args, **kwargs):
        super(SearchArgsSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://search.yahoo.co.jp/search?p=' + query]
        self.rank = int(rank)

    def parse(self, response):
        w = response.css('div#WS2m div.w')[self.rank]
        d = {}
        d['rank'] = self.rank
        d['comment'] = self.comment
        d['title'] = w.css('h3 a').xpath('string()').extract_first()
        d['url'] = 'https://' + w.css('div.a span.u').xpath('string()').extract_first()
        yield d

# -*- coding: utf-8 -*-
import scrapy


class SearchSingleSpider(scrapy.Spider):
    name = 'search_single'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['https://search.yahoo.co.jp/search?p=python']

    def parse(self, response):
        for i, w in enumerate(response.css('div#WS2m div.w')):
            d = {}
            d['rank'] = i
            d['title'] = w.css('h3 a').xpath('string()').extract_first()
            d['url'] = 'https://' + w.css('div.a span.u').xpath('string()').extract_first()
            yield d

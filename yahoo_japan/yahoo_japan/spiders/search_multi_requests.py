# -*- coding: utf-8 -*-
import scrapy


class SearchMultiRequestsSpider(scrapy.Spider):
    name = 'search_multi_requests'
    allowed_domains = ['yahoo.co.jp']

    def start_requests(self):
        with open('list.txt') as f:
            for q in f:
                yield scrapy.Request('https://search.yahoo.co.jp/search?p=' + q)

    def parse(self, response):
        for i, w in enumerate(response.css('div#WS2m div.w')):
            d = {}
            d['rank'] = i
            d['title'] = w.css('h3 a').xpath('string()').extract_first()
            d['url'] = 'https://' + w.css('div.a span.u').xpath('string()').extract_first()
            yield d

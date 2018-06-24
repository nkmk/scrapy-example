# -*- coding: utf-8 -*-
import scrapy


class TopicsSpider(scrapy.Spider):
    name = 'topics'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://yahoo.co.jp/']

    def parse(self, response):
        pass

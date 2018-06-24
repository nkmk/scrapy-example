# -*- coding: utf-8 -*-
import scrapy


class TopicsDetailSpider(scrapy.Spider):
    name = 'topics_detail'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://yahoo.co.jp/']

    def parse(self, response):
        pass

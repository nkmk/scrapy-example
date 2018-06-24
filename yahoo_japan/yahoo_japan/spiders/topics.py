# -*- coding: utf-8 -*-
import scrapy
from yahoo_japan.items import YahooJapanItem


class TopicsSpider(scrapy.Spider):
    name = 'topics'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://yahoo.co.jp/']

    def parse(self, response):
        for topic in response.css('div#topicsfb ul.emphasis li'):
            item = YahooJapanItem()
            item['headline'] = topic.css('a::text').extract_first()
            item['url'] = topic.css('a::attr(href)').extract_first()
            yield item

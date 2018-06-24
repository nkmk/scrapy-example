# -*- coding: utf-8 -*-
import scrapy
from yahoo_japan.items import YahooJapanDetailItem


class TopicsDetailSpider(scrapy.Spider):
    name = 'topics_detail'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://yahoo.co.jp/']

    def parse(self, response):
        for topic in response.css('div#topicsfb ul.emphasis li'):
            item = YahooJapanDetailItem()
            item['headline'] = topic.css('a::text').extract_first()
            yield scrapy.Request(topic.css('a::attr(href)').extract_first(),
                                 callback=self.parse_detail,
                                 meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        item['url'] = response.url
        item['title'] = response.css('div.topicsDetail h2 a::text').extract_first()
        yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yahoo_japan.items import YahooJapanNewsItem


class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    rules = (
        Rule(
            LinkExtractor(restrict_css='ul#gnSec'),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        category = response.css('ul#gnSec li.current a::text').extract_first()
        for topic in response.css('div#epTabTop ul.topics h1.ttl, p.ttl'):
            item = YahooJapanNewsItem()
            item['headline'] = topic.css('a::text').extract_first()
            item['url'] = topic.css('a::attr(href)').extract_first()
            item['category'] = category
            yield item

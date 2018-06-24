# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yahoo_japan.items import YahooJapanNewsDetailItem


class NewsCrawlDetailSpider(CrawlSpider):
    name = 'news_crawl_detail'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    rules = (
        Rule(
            LinkExtractor(restrict_css='ul#gnSec'),
        ),
        Rule(
            LinkExtractor(restrict_css='div#epTabTop ul.topics h1.ttl, p.ttl'),
            callback='parse_item'
        )
    )

    def parse_item(self, response):
        item = YahooJapanNewsDetailItem()
        item['url'] = response.url
        item['title'] = response.css('div.topicsDetail h2 a::text').extract_first()
        item['category'] = response.css('ul#gnSec li.current a::text').extract_first()
        return item

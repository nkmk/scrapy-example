# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooJapanItem(scrapy.Item):
    headline = scrapy.Field()
    url = scrapy.Field()


class YahooJapanDetailItem(scrapy.Item):
    headline = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()


class YahooJapanNewsItem(scrapy.Item):
    url = scrapy.Field()
    headline = scrapy.Field()
    category = scrapy.Field()

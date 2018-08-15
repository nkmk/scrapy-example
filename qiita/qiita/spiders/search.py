# -*- coding: utf-8 -*-
import scrapy
import datetime


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['qiita.com']
    rank = 0
    count = 0

    def __init__(self, query='', limit=1, date_from='2011-01-01', date_to=None, sort='stock', *args, **kwargs):
        super(SearchSpider, self).__init__(*args, **kwargs)
        q = query + '+created%3A%3E' + date_from
        if date_to:
            q += '+created%3A%3C' + date_to
        self.start_urls = ['https://qiita.com/search?utf8=%E2%9C%93&sort={}&q={}'.format(sort, q)]
        self.limit = int(limit)

    def parse(self, response):
        base_url = 'https://qiita.com'
        for result in response.css('div.searchResultContainer_main div.searchResult'):
            d = {}

            result_main = result.css('div.searchResult_main')
            url = result_main.css('h1.searchResult_itemTitle a::attr(href)').extract_first()
            _, user_id, _, article_id = url.split('/')
            title = result_main.css('h1.searchResult_itemTitle a').xpath('string()').extract_first()
            date_s_en = result_main.css('div.searchResult_header::text').extract_first().split(' posted at ')[-1]
            date_s = datetime.datetime.strptime(date_s_en, '%b %d, %Y').strftime('%Y-%m-%d')
            tag_list = ','.join(result_main.css('ul.tagList li a::text').extract())

            result_sub = result.css('div.searchResult_sub')
            status_list = [li.css('::text').extract_first().strip()
                           for li in result_sub.css('ul.searchResult_statusList li')]
            likes = 0
            comments = 0
            if len(status_list) > 0:
                likes = status_list[0]
            if len(status_list) > 1:
                comments = status_list[1]
            
            d['rank'] = self.rank
            self.rank += 1
            d['title'] = title
            d['user_id'] = user_id
            d['article_id'] = article_id
            d['date'] = date_s
            d['likes'] = likes
            d['comments'] = comments
            d['tag'] = tag_list
            d['url'] = base_url + url
            yield d

        next_url = response.css('ul.pagination li a.js-next-page-link::attr(href)').extract_first()
        self.count += 1
        if next_url and self.count < self.limit:
            yield scrapy.Request(base_url + next_url)

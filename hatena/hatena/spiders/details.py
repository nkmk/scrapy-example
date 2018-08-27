import time
import requests
import scrapy


class DetailsSpider(scrapy.Spider):
    name = 'details'
    allowed_domains = ['b.hatena.ne.jp']

    def __init__(self, url, sleep_sec=1, *args, **kwargs):
        super(DetailsSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://b.hatena.ne.jp/entrylist?sort=eid&url=' + url]
        self.sleep_sec = sleep_sec

    def parse(self, response):
        for li in response.css('div.entrylist-main li.js-keyboard-selectable-item'):
            d = {}
            url = li.css('h3.entrylist-contents-title a::attr(href)').extract_first()
            d['url'] = url

            time.sleep(self.sleep_sec)
            r = requests.get('http://b.hatena.ne.jp/entry/jsonlite/', params={'url': url})
            j = r.json()
            d['title'] = j['title']
            for b in j['bookmarks']:
                d.update(b)
                d['tags'] = ','.join(d['tags'])
                yield d

        next_url = response.css('p.entrylist-readmore a::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request('http://b.hatena.ne.jp' + next_url)

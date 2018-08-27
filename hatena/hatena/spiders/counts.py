import scrapy


class CountsSpider(scrapy.Spider):
    name = 'counts'
    allowed_domains = ['b.hatena.ne.jp']

    def __init__(self, url, *args, **kwargs):
        super(CountsSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://b.hatena.ne.jp/entrylist?sort=eid&url=' + url]

    def parse(self, response):
        for li in response.css('div.entrylist-main li.js-keyboard-selectable-item'):
            d = {}
            d['url'] = li.css('h3.entrylist-contents-title a::attr(href)').extract_first()
            d['count'] = li.css('span.entrylist-contents-users a span::text').extract_first()
            yield d

        next_url = response.css('p.entrylist-readmore a::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request('http://b.hatena.ne.jp' + next_url)

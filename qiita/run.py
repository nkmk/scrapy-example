from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

settings.set('FEED_FORMAT', 'csv')
settings.set('FEED_URI', 'results/%(filename)s.csv')

configure_logging()
runner = CrawlerRunner(settings)

tags = ['Python', 'Ruby']


@defer.inlineCallbacks
def crawl():
    for tag in tags:
        yield runner.crawl('search', query='tag:' + tag,
                           limit=2, start_date='2015-01-01', end_date='2015-12-31',
                           filename=tag.lower() + '_2015_top20')
    reactor.stop()


crawl()
reactor.run()

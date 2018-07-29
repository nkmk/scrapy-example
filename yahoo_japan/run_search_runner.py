from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

settings.set('FEED_URI', 'results/search_%(filename)s_%(rank)s.csv')

configure_logging()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    yield runner.crawl('search_args', query='python', rank=0, comment='test', filename='python')
    yield runner.crawl('search_args', query='ruby', rank=0, comment='test', filename='ruby')
    reactor.stop()


crawl()
reactor.run()

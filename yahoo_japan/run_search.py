from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

settings.set('FEED_URI', 'results/search_%(filename)s_%(rank)s.csv')

process = CrawlerProcess(settings)
process.crawl('search_args', query='python', rank=0, comment='test', filename='python')
process.crawl('search_args', query='ruby', rank=0, comment='test', filename='ruby')
process.start()

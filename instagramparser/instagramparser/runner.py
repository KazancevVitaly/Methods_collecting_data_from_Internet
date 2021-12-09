from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from instagramparser import settings
from instagramparser.spiders.instagramspider import InstagramspiderSpider

if __name__ == '__main__':

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(InstagramspiderSpider)
    crawler_process.start()

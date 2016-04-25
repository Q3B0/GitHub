#encoding:utf-8

from coolscrapy.items import HuxiuItem
import scrapy

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domain = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/index.php"
    ]


    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            item['title'] = str(sel.xpath('h3/a/text()')[0].extract()).encode('utf-8')
            item['link'] = sel.xpath('h3/a/@href')[0].extract().encode('utf-8')
            url = response.urljoin(item['link'])
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract().encode('utf-8')
            yield scrapy.Request(url, callback=self.parse_artical)

    def parse_artical(self, response):
        response.body.decode(response.encoding)
        detail = response.xpath('//div[@class="article-wrap"]')
        item = HuxiuItem()
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['link'] = response.url
        item['posttime'] = detail.xpath(
            'div[@class="article-author"]/span[@class="article-time"]/text()')[0].extract()
        print(item['title'], item['link'], item['posttime'])
        yield item
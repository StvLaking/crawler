# -*- coding: utf-8 -*-
import scrapy
import json
import re
from scrapy.selector import Selector
try:
	from scrapy.spider import Spider
except:
	from scrapy.spider import BaseSpider as Spider
	

class ScrapyOrgSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = (
		"http://hr.tencent.com/position.php"
    )
#rules of crawler
	rules = [
		Rule(sle(allow("position.php\?&start=\d{,4}#a")),
				 follow=True,
				 callback='parse_item')
		]

## rules in callback
    def parse_item(self, response):
		items=[]
		sel = Selector(response)
		base_url=get_base_url(response)
		sites_even =sel.css('table.tablelist tr.even')
		for site in sites_even:
			item = JobItem()
			item['name']=site.css('.l.square a').xpath('text()').extract()
			relative_url=site.css('.l.square a').xpath('@href').extract()
			item['detailLink']=urljoin_rfc(base_url,relative_url)
			item['catalog']=site.css('tr > td:nth-child(2)::text').extract()


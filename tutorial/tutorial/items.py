scovered open port 143/tcp on 220.181.90.34
Discovered open port 110/tcp on 220.181.90.34
Discovered open port 993/tcp on 220.181.90.34
Discovered open port 80/tcp on 220.181.90.34
Discovered open port 443/tcp on 220.181.90.34
Discovered open port 995/tcp on 220.181.90.34
Discovered open port 465/tcp on 220.181.90.34

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
	title=scrapy.Field()
	link=scrapy.Field()
	desc=scrapy.Field()

class ArticleItem(scrapy.Item):
	title=scrapy.Field()
	link=scrapy.Field()
	desc=scrapy.Field()


	class JobItem(scrapy.Item):
		name = Field()
		catalog = Field()
		workLocation = Field()
		recruitNumber = Field()
		detailLink = Field()
		publishTime = Field()


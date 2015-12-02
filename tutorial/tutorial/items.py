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

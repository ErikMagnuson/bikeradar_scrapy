from scrapy.spiders import SitemapSpider
from scrapy.loader import ItemLoader
from ..items import Bike


#class BikeradarSpider(scrapy.Spider):
class BikeradarSpider(SitemapSpider):
    name = 'bikeradar'
    allowed_domains = ['bikeradar.com']
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 2}

    # start_urls = ['https://www.bikeradar.com/reviews/bikes/road-bikes/giant-defy-advanced-0-review/',]
    sitemap_urls = ['https://www.bikeradar.com/wp-sitemap-posts-reviews-1.xml']
    sitemap_rules = [
        ('/reviews/bikes/', 'parse_review')
    ]

    def parse_review(self, response):
        l = ItemLoader(item=Bike(), response=response)
        l.add_xpath(
            'name', '//td[@class="spec-table__label"][text()="Name"]/following-sibling::td/text()')
        l.add_xpath(
            'brand', '//td[@class="spec-table__label"][text()="Brand"]/following-sibling::td/text()')
        l.add_xpath(
            'rating', '//span[@class="ratings-stars__value"]/span[@class="sr-only"]/text()')
        l.add_value('image_urls', response.xpath('//figure//img/@src').get())
        return l.load_item()
            
            
#'name' : response.css('.template-article__im-products-schema-microdata').xpath('.//*[@itemprop="name"]/text()').get(),
#'brand' : response.css('.template-article__im-products-schema-microdata').xpath('.//*[@itemprop="brand"]/text()').get(),
#'model' : response.css('.template-article__im-products-schema-microdata').xpath('.//*[@itemprop="model"]/text()').get(),
#'category' : response.css('.template-article__im-products-schema-microdata').xpath('.//*[@itemprop="category"]/text()').get(),
#'sku' : response.css('.template-article__im-products-schema-microdata').xpath('.//*[@itemprop="sku"]/text()').get(),
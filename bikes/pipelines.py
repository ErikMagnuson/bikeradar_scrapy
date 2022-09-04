from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from urllib.parse import urlparse

class BikesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('image_urls'):
            o = urlparse(adapter['image_urls'][0])
            adapter['image_urls'][0] = o.scheme + "://" + o.netloc + o.path
            return item
        else: DropItem(f"Missing image url in {item}")
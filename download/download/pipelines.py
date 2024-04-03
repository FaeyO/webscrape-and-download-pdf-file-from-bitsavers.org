# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import mimetypes
from pathlib import Path

class DownloadPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        urls = ItemAdapter(item).get(self.files_urls_field, [])
        return [Request(u, meta={'file_name': item.get('filename')}) for u in urls] #callback=NO_CALLBACK
    def file_path(self, request, response=None, info=None, *, item=None):
        #media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        media_ext = Path(request.url).suffix

        # Handles empty and wild extensions by trying to guess the
        # mime type then extension or default to empty string otherwise
        if media_ext not in mimetypes.types_map:
            media_ext = ""
            media_type = mimetypes.guess_type(request.url)[0]
            if media_type:
                media_ext = mimetypes.guess_extension(media_type)
        return f"full/{request.meta['file_name']}{media_ext}"
        #return f"full/{media_guid}{media_ext}"
    
    # def process_item(self, item, spider):
    #     return item

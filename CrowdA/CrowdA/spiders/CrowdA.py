import scrapy 
from CrowdA.items.crowdaItem import CrowdaItem

class CrowdA(scrapy.Spider):
    name = "crowdA"
    
    start_urls = ["https://www.grainger.com/category/hardware/braces-and-brackets?categoryIndex=1"]
    
    def parse(self, response):
        # Print the status code of the response
        print("[Received]")
      
        data = response.css("div._2LiIQ9 div.DDuvHw")
        if not data:
            self.logger.error("No data found for the selector.")
        else:
            for div in data:
                item = CrowdaItem()
                item['title'] = div.css("span a::attr(title)").get()
                yield item
        # data = response.xpath("//div[contains(@class, '_2LiIQ9')]//div[contains(@class, 'DDuvHw')]")
        # if not data:
        #     self.logger.error("No data found for the selector.")
        # else:
        #     for div in data:
        #         lis = div.xpath('.//ul//li/a')
        #         self.logger.info(lis)
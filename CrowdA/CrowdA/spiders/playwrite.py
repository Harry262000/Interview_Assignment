import scrapy
from scrapy_playwright.page import PageMethod

# Import the CrowdAItem class from items.py
from CrowdA.items import CrowdAItem

def should_abort_request(request):
    if request.resource_type == "image":
        return True
    if request.method.lower() == 'post':
        return True
    return False


class CrowdASpider(scrapy.Spider):
    name = 'crowdAP'
    
    custom_settings = {
        'PLAYWRIGHT_ABORT_REQUEST' : should_abort_request
    }

    def start_requests(self):
        # URL to start scraping
        url = "https://www.grainger.com/category/hardware/braces-and-brackets?categoryIndex=1"
        
        # Set up request with meta data including Playwright configurations
        request = scrapy.Request(url, meta={
            'playwright': True,
            'playwright_include_page': True,
            #'playwright_page_methods': [PageMethod('wait_for_selector', '.RizBES',timeout=60000)],
            'playwright_page_methods': [
                PageMethod("wait_for_selector", "li.pan5o1"), 
                PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                #PageMethod("wait_for_selector", "div.quote:nth-child(11)")
            ],
            'errback': self.errback,
            # Ensure playwright_page is included
        })
        yield request

    async def parse(self, response):
        # Ensure the 'playwright_page' key is present in the meta dictionary
        page = response.meta.get("playwright_page")
        if not page:
            self.logger.error("Playwright page is None")
        else:
            # Close the Playwright page
            await page.close()
            self.logger.info("================================")
            print("===========================")
            print(response)
                #self.logger.info(quote)

    async def errback(self, failure):
        # Handle errors and close the Playwright page
        page = failure.request.meta.get("playwright_page")
        if page:
            await page.close()
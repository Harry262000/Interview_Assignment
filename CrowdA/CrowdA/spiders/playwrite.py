import scrapy
from scrapy_playwright.page import PageMethod
from quotes_js_scraper.items import QuoteItem

class CrowdASpider(scrapy.Spider):
    name = 'crowdAP'

    def start_requests(self):
        url = "https://www.grainger.com/category/hardware/braces-and-brackets?categoryIndex=1"
        yield scrapy.Request(url, meta={
            'playwright': True,
            'playwright_include_page': True,
            'playwright_page_methods': [PageMethod('wait_for_selector', 'div.quote')],
            'errback': self.errback,
        })

    async def parse(self, response):
        page = response.meta["playwright_page"]
        data = await page.querySelectorEval('li.pan5o1', 'element.textContent')
        print("==============================")
        print(data)
        # Instantiate QuoteItem and extract data as needed
        # quote_item = QuoteItem()
        # quote_item['text'] = data
        # yield quote_item

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()

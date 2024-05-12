import scrapy
import json

class CrowdA(scrapy.Spider):
    name = 'crowdA'
    start_urls = ['https://www.grainger.com/category/hardware/braces-and-brackets?categoryIndex=1']  # Start URL of the website (optional)

    def start_requests(self):
        api_url = 'https://www.grainger.com/product/info?productArray=1WDD1%2C1WDD2%2C1WDD3%2C1WDD4%2C1WDD5%2C1WDD6%2C1WDD7%2C1WDD8%2C1WDD9%2C1WDE1%2C1WDE3%2C1WDE4%2C1WDE5%2C1WDE6%2C1WDE7%2C1WDF1%2C1WDF4%2C1WDF5%2C1WDF6%2C1WDF7%2C1WDF8%2C1WDG3%2C1WDG6%2C1WDG8%2C1WDG9%2C1WDH2%2C1WDH3%2C1WDH9%2C1WDJ4%2C1WDJ5%2C1WDJ6%2C1WDK4%2C1WDK5%2C1WDK6%2C1WDK7%2C1WDK8%2C1WDK9%2C1WDL1%2C1WDL3%2C1WDL4%2C1WDL8%2C1WDL9%2C1WDN1%2C1XMP3%2C1XMP4%2C3HJH3%2C3HJH4%2C4PB60%2C4PB61%2C4PB62&_=1715448397189'
        headers = {'Authorization': 'Bearer YOUR_API_TOKEN'}
        yield scrapy.Request(api_url, headers=headers, callback=self.parse_api_response)

    def parse_api_response(self, response):
        # Parse JSON response
        data = json.loads(response.body)
        print(type(data))
        for item in data:
            product = data[item] 
            if type(product) == dict and item != "categoryAnalytics":
                
                yield {
                    'category_No': product['catalogGroupNumber'],
                    'Picture_url': product['pictureUrl'],
                }
            
            




































        
                
                
                
                
                
                
                
                
                
                
                
                
            
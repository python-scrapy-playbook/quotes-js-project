import scrapy
from quotes_js_scraper.items import QuoteItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class QuotesSpider(scrapy.Spider):
    name = 'quotes_3'

    def start_requests(self):
        url = 'https://www.twitchmetrics.net/channels/viewership?game=Sports'
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('h5.mr-2.mb-0'):
            quote_item['text'] = quote.css('::text').get()
            # Transform the scraped data into the desired format
            transformed_data = f'twitch.tv/{quote_item["text"]}/about'
            # Yield the transformed data
            yield {'transformed_data': transformed_data}

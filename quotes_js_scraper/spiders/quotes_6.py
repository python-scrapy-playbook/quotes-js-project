import scrapy
from quotes_js_scraper.items import QuoteItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class QuotesSpider(scrapy.Spider):
    name = 'quotes_6'

    start_urls = [
        'https://www.twitch.tv/kingsleague/about', 
'https://www.twitch.tv/BALLERLEAGUE/about', 'https://www.twitch.tv/scump/about'
        # Add more URLs as strings separated by commas
    ]
    def start_requests(self):
        # Iterate over the list of URLs and yield SeleniumRequest for each
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('a[data-test-selector="link_url_test_selector"]::attr(href)'):
            quote_item['text'] = quote.css('::text').get()
            yield {'name': quote_item}




    
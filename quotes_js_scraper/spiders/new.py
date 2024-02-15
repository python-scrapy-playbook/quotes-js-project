import scrapy
from quotes_js_scraper.items import QuoteItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class QuotesSpider(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = [
        'https://www.twitch.tv/scump/about'

        # Add more URLs as strings separated by commas
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url, 
                callback=self.parse,
                wait_time=3,  # Waits for 3 seconds after the page has loaded
                wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, '.Layout-sc-1xcs6mc-0.channel-panels'))
            )

    def parse(self, response):
        container = response.css('.Layout-sc-1xcs6mc-0.channel-panels')
        for link in container.css('a.ScCoreLink-sc-16kq0mq-0.eFqEFL.tw-link'):
            text = link.css('::text').get()
            href = link.attrib['href']
            yield {
                'text': text,
                'url': href
            }
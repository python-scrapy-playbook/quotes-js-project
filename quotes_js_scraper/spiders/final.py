from scrapy import Spider
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time

class YourSpiderWithSelenium(Spider):
    name = 'final_1'
    start_urls = ['https://www.twitch.tv/scump/about']

    def __init__(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)

    def start_requests(self):
        for url in self.start_urls:
            self.driver.get(url)
            time.sleep(10)  # Adjust the timing based on your needs
            self.parse_response(self.driver.page_source, self.driver.current_url)

    def parse_response(self, body, current_url):
        # Instead of yielding HtmlResponse, parse the page source directly here
        # For demonstration, let's say you're extracting and printing URLs
        response = HtmlResponse(url=current_url, body=body, encoding='utf-8')
        links = response.xpath('//a[@data-test-selector="link_url_test_selector"]/@href').getall()
        for link in links:
            yield {'url': link}


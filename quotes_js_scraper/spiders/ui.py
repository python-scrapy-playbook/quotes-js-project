import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Importing time for sleep

class QuotesSpider(scrapy.Spider):
    name = 'detailed_navigation_spider_with_delays'
    start_urls = ['https://www.twitch.tv/scump/about']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # Simulate waiting for the content to load
        self.logger.info("Waiting for content to load...")
        time.sleep(1)  # Wait for 1 second before proceeding

        # Navigate to the desired containers with waiting in between
        containers = response.css('.Layout-sc-1xcs6mc-0.cRYXMq .Layout-sc-1xcs6mc-0.jBLVus .ScTransitionBase-sc-hx4quq-0.OBUFH .Layout-sc-1xcs6mc-0.daZyRV .Layout-sc-1xcs6mc-0.ceSMVf .Layout-sc-1xcs6mc-0.gXxRYI[data-a-target="about-panel"] .Layout-sc-1xcs6mc-0.frPaLE .Layout-sc-1xcs6mc-0.channel-panels')
        
        for container in containers:
            # Introduce a delay between processing each container
            time.sleep(1)  # Wait for 1 second to ensure content is fully loaded
            
            links = container.css('a.ScCoreLink-sc-16kq0mq-0.eFqEFL.tw-link')
            for link in links:
                href = link.attrib['href']
                text = link.css('::text').get(default='No text')
                yield {
                    'text': text,
                    'url': href
                }
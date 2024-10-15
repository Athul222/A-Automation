import requests
import lxml 
from bs4 import BeautifulSoup

class ScrapWebsite:
    def __init__(self, url: str, element: str):
        self.url = url
        self.element_to_scrape = element
        
    def scrape(self):
        response = requests.get(url=self.url)
        website = response.text
        soup = BeautifulSoup(website, "lxml")
        
        elements = soup.select(selector=self.element_to_scrape)
        elements_content_list = [content.get_text() for content in elements]
        return elements_content_list
        
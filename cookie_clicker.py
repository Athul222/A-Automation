from selenium import webdriver
from selenium.webdriver.common.by import By
import time

COOKIE_URL = "https://orteil.dashnet.org/experiments/cookie/"

class CookieClicker:
    def __init__(self, minute: int):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options)
        self.minute = minute
        
    def run(self):
        self.driver.get(url=COOKIE_URL)
        cookie = self.driver.find_element(By.ID, value="cookie")

        items = self.driver.find_elements(By.CSS_SELECTOR, value="#store div")
        item_ids = [item.get_attribute("id") for item in items]

        timeout = time.time() + 5
        play_minute = time.time() + 60 * self.minute  # 5-minutes

        while True:
            cookie.click()
            
            # Every 5 seconds:
            if time.time() > timeout:
                
                # get all upgrade <b> tags
                all_prices = self.driver.find_elements(By.CSS_SELECTOR, value= "#store b")
                item_prices = []
                
                # convert <b> text into an integer price
                for price in all_prices:
                    element_text = price.text
                    if element_text != "":
                        cost = int(element_text.split("-")[1].strip().replace(",", ""))
                        item_prices.append(cost)

                # Create dictionary to store items and prices
                cookie_upgrade = {}
                for n in range(len(item_prices)):
                    cookie_upgrade[item_prices[n]] = item_ids[n]
                    
                # Get current cookie count
                money_element = self.driver.find_element(By.ID, value="money").text
                if "," in money_element:
                    money_element = money_element.replace(",", "")
                cookie_count = int(money_element)
                
                # Find upgrades that we can currently afford.
                affordable_upgrades = {}
                for cost, id in cookie_upgrade.items():
                    if cookie_count > cost:
                        affordable_upgrades[cost] = id
                
                # Purchase the most expensive affordable upgrade
                highest_price_affordable_upgrade = max(affordable_upgrades)
                print(highest_price_affordable_upgrade)
                
                to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
                
                self.driver.find_element(By.ID, value= to_purchase_id).click()
                
                # Add another 5 seconds until the next check
                timeout = time.time() + 5
            
            # After 5 minutes stop the bot and check the cookies per second count
            if time.time() > play_minute:
                cookie_per_s = self.self.driver.find_element(By.ID, value="cps").text
                print(cookie_per_s)
                break

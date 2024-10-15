import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class InternetSpeedTwitterBot:
    def __init__(self, promised_up: int, promised_down: int, email: str, username: str, password: str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        chrome_driver = webdriver.Chrome(options=chrome_options)
        self.promised_up = promised_up
        self.promised_down = promised_down
        self.twitter_email = email
        self.twitter_username = username
        self.twitter_password = password
        self.driver = chrome_driver
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        time.sleep(2)
        accept_button = self.driver.find_element(
            By.CSS_SELECTOR, 
            value="#onetrust-accept-btn-handler")
        accept_button.click()
        
        time.sleep(2)
        go_button = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=".start-button a"
        )
        go_button.click()
        
        time.sleep(60)
        self.up = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text
        print("UPLOAD SPEED => ", self.up)
        
        self.down = self.driver.find_element(
            By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        ).text
        print("DOWNLOAD SPEED => ", self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        
        time.sleep(6)
        email = self.driver.find_element(
            By.NAME,
            value='text'
        )
        email.send_keys(self.twitter_email)
        time.sleep(1)
        email.send_keys(Keys.ENTER)
        
        try:
            time.sleep(2)
            username_entry_btn = self.driver.find_element(
                By.CSS_SELECTOR,
                value='#react-root div input'
            )
            username_entry_btn.send_keys(self.twitter_username)
            username_entry_btn.send_keys(Keys.ENTER)
        except NoSuchElementException:
            time.sleep(2)
            
        time.sleep(3)
        password = self.driver.find_element(
            By.NAME,
            value='password'
        )
        password.send_keys(self.twitter_password)
        password.send_keys(Keys.ENTER)
        
        time.sleep(5)
        tweet_compose = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        )
        tweet_compose.click()
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promised_down}down/{self.promised_up}up?"
        time.sleep(3)
        tweet_entry_area = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        )
        tweet_entry_area.send_keys(tweet)
        
        try:
            time.sleep(3)
            tweet_button = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div')
            tweet_button.click()
            print("Tweeted!")
        except NoSuchElementException or ElementClickInterceptedException:
            time.sleep(2)
            close_notification_btn = self.driver.find_element(
                By.CSS_SELECTOR,
                value='#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-rsyp9y.r-1pjcn9w > div > div > div > div.css-175oi2r.r-gtdqiz.r-ipm5af.r-136ojw6 > div > div > div > div > div > div.css-175oi2r.r-1pz39u2.r-1777fci.r-15ysp7h.r-1habvwh.r-s8bhmr > button'
            )
            close_notification_btn.click()
        
        time.sleep(2)
        self.driver.quit()


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# instagram URL 
INSTAGRAM_PATH = "https://www.instagram.com/accounts/login/"

class InstagramFollowerBot:
    def __init__(self, username: str, password: str, similar_account: str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_driver = webdriver.Chrome(options= chrome_options)
        self.driver = chrome_driver
        self.instagram_username = username
        self.instagram_password = password
        self.similar_account = similar_account
        
    def instagram_login(self):
        self.driver.get(url= INSTAGRAM_PATH)
        sleep(2)
        username_field = self.driver.find_element(By.NAME, value="username")
        username_field.send_keys(self.instagram_username)
        password_field = self.driver.find_element(By.NAME, value="password")
        password_field.send_keys(self.instagram_password)
        password_field.send_keys(Keys.ENTER)
        sleep(4)
            
    def find_followers(self):
        sleep(3)
        try:
            cancel_save_your_login_button = self.driver.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
            notification_button = self.driver.find_element(By.XPATH, 
                                 value="//button[contains(text(), 'Not Now')]")
        except Exception:
            print(Exception)
        else:
            cancel_save_your_login_button.click()
            sleep(1)
            notification_button.click()
                        
        sleep(1)
        self.driver.get(url= f"https://www.instagram.com/{self.similar_account}/followers/")
        
        sleep(1)
        click_followers_view = self.driver.find_element(
            by=By.XPATH,
            value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a'
        )
        click_followers_view.click()
        
        # Scrowling down the pop up
        sleep(3)
        modal_xpath = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'
        modal = self.driver.find_element(by=By.XPATH, value= modal_xpath)
        modal_height = modal.size["height"]
        print("HEIGHT => ", modal_height)
        for i in range(0, modal_height, 10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[1]", modal, 100)
            sleep(0.7)
        
    def follow(self):
        sleep(3)
        followers_list = self.driver.find_elements(
            by=By.CSS_SELECTOR, 
            value="body > div.xhu9ww4.xidawru.x13ywhbb.x1dbek64.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 > div:nth-child(2) > div button")
        # print("Follower list => ", followers_list)
        for user in followers_list:
            if user.text.lower() == "follow":
                print("Not following")
                try:
                    user.click()
                    sleep(1)
                except ElementClickInterceptedException:
                    print("Already followed")
                    cancel_button = self.driver.find_element(by=By.XPATH, 
                                                            value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                    sleep(1.1)
            else:
                print("Already requested/followed!")
        print("Done!")
        self.driver.quit()


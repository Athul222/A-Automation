from time import sleep
from dotenv import load_dotenv, dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class TinderBot:
    def __init__(self, username: str, password: str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options= chrome_options)
        self.driver = driver
        self.facebook_id = username
        self.facebook_password = password
    
    def run(self):   
        self.driver.get("https://tinder.com/")
        sleep(3)
        cookie_popup = self.driver.find_element(
            By.XPATH,
            value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button"
            )
        cookie_popup.click()
        
        sleep(2)
        login_button = self.driver.find_element(
            by=By.CSS_SELECTOR, 
            value="#u-1804268477 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div:nth-child(2) > a"
        )
        login_button.click()
        
        sleep(2)
        more_options = self.driver.find_element(
            By.XPATH, 
            value='/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button')
        more_options.click()
         
        try:
            sleep(2)
            facebook_signin_button = self.driver.find_element(
                By.XPATH,
                value='/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        except NoSuchElementException:
            sleep(1)
            account_recovery_btn = self.driver.find_element(
                By.XPATH,
                value="/html/body/div[2]/div/div/div[2]/button"
            )
            account_recovery_btn.click()
            
            login_button = self.driver.find_element(
                by=By.CSS_SELECTOR, 
                value="#u-1804268477 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div:nth-child(2) > a"
            )
            login_button.click()
            sleep(2)
            facebook_signin_button = self.driver.find_element(
                By.XPATH,
                value='/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
            facebook_signin_button.click()
            
            sleep(1)
            more_options = self.driver.find_element(
                By.XPATH, 
                value='/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/button')
            more_options.click()
        else:
            facebook_signin_button.click()
        # self.driver.window_handles  => return list of windows 
        # tinder window[Base window]
        sleep(2)
        base_window = self.driver.window_handles[0]

        # facebook window[2nd oppened window]
        # switching the selenium self.driver to the fb window so we can log in fb
        fb_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_login_window)
        print(self.driver.title) # prints the title of current selenium controlled window 

        # Login to fb
        sleep(4)
        email_field = self.driver.find_element(By.NAME, value='email')
        email_field.send_keys(self.facebook_id)
        password_field = self.driver.find_element(By.NAME, value='pass')
        password_field.send_keys(self.facebook_password)
        password_field.send_keys(Keys.ENTER)
        
        try:
            self.driver.implicitly_wait(4)
            continue_as_btn = self.driver.find_element(
                by=By.XPATH, 
                value="/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div"
            )
            continue_as_btn.click()
        except NoSuchElementException:
            sleep(2)
        else:
            # reverting back to the base window[tinder in our case]
            self.driver.switch_to.window(base_window)
            print(self.driver.title)

            sleep(5)
            allow_location_button = self.driver.find_element(
                By.XPATH, 
                value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
            allow_location_button.click()
            sleep(3)
            reject_notification_button = self.driver.find_element(
                By.XPATH, 
                value='/html/body/div[2]/div/div/div/div/div[3]/button[2]')
            sleep(2)
            reject_notification_button.click()
            
            sleep(2)       
            for _ in range(10):
                sleep(3)
                try:
                    hit_like = self.driver.find_elements(
                        By.XPATH, 
                        value='/html/body/div[1]/div/div[1]/div//button'
                    )
                    class_element = 'button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style gamepad-button Bxsh($bxsh-btn) Expand Ov(h) Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a'
                    for i in hit_like:
                        if i.get_attribute("class") == class_element:
                            i.click()
                except ElementClickInterceptedException:
                    try:
                        add_tinder_to_home_screen_btn = self.driver.find_element(
                            By.XPATH, 
                            value="/html/body/div[2]/div/div/div[2]/button[2]"
                        )
                        add_tinder_to_home_screen_btn.click()  
                          
                    except NoSuchElementException:
                        try:
                            match_popup = self.driver.find_element_by_css_selector(".itsAMatch a")
                            match_popup.click()
                        except NoSuchElementException:
                            sleep(2)

            sleep(4)
            print("Like limit has reached. Upgrade to premium for unlimitted like per day!")
            self.driver.quit()
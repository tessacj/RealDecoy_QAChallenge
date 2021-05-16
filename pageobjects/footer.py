from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from values import strings

class Footer:
    def __init__(self, driver):
        self.driver = driver

        self.twitter_icon = WebDriverWait(self.driver.instance, 10).until(EC.element_to_be_clickable((
            By.CLASS_NAME, "social_twitter")))

        self.facebook_icon = WebDriverWait(self.driver.instance, 10).until(EC.element_to_be_clickable((
            By.CLASS_NAME, "social_facebook")))
        
        self.linkedin_icon = WebDriverWait(self.driver.instance, 10).until(EC.element_to_be_clickable((
            By.CLASS_NAME, "social_linkedin")))
        
        # self.terms_service = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
        #     By.CLASS_NAME, "login_logo")))

        # self.privacy_policy = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
        #     By.CLASS_NAME, "login_logo")))
    
    def twitter_check(self):
        assert self.twitter_icon.is_displayed()
        self.twitter_icon.click()

    def facebook_check(self):
        assert self.facebook_icon.is_displayed()
        self.facebook_icon.click()
    
    def linkedin_check(self):
        assert self.linkedin_icon.is_displayed()
        self.linkedin_icon.click()
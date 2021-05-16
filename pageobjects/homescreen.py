from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pytest


from values import strings


class HomeScreen:
    
    def __init__(self, driver):
        self.driver = driver

        self.icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "login_logo")))

        self.login_username = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.ID, "user-name")))

        self.login_password = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.ID, "password")))

        self.login_button = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.ID, "login-button")))

        self.credentials = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "login_credentials_wrap-inner")))
        
        
        # self.error_msg = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
        #     By.CLASS_NAME, "error-button")))

    def validate_page_loaded(self):
        assert self.icon.is_displayed()
        assert self.login_username.is_displayed()
        assert self.login_password.is_displayed()
        assert self.login_button.is_displayed()
        assert self.credentials.is_displayed()

    def standard_user_login(self):
        self.login_username.send_keys(strings.standard_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()
        
        # self.successfull_login = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
        #     By.XPATH, "//*[@id='header_container']/div[2]/span")))

        # assert self.successfull_login.is_displayed()
        # assert self.successfull_login.text == "Products", "Login Unsuccessful"

    def locked_out_user_login(self):
        self.login_username.send_keys(strings.locked_out_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()

        self.error_msg = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "error-button")))

        assert self.error_msg.is_displayed()

    def problem_user_login(self):
        self.login_username.send_keys(strings.problem_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()

        self.successfull_login = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "title")))

        assert self.successfull_login.is_displayed()
    
    def performance_glitch_user_login(self):
        self.login_username.send_keys(strings.performance_glitch_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()

        # self.backendPerformance = self.responseStart - self.navigationStart
        # self.frontendPerformance = self.domComplete - self.responseStart

        # assert self.frontendPerformance > 2, "The user may be experiencing performance issues relating to the frontend"
        # assert self.backendPerformance > 2, "The user may be experiencing performance issues relating to the backend"
        try:
            self.successfull_login = WebDriverWait(self.driver.instance, 3).until(EC.visibility_of_element_located((
                By.CLASS_NAME, "title")))
        except TimeoutException:
            assert False, "The user may be experiencing performance issues"

        # assert self.successfull_login.is_displayed()
        # assert self.successfull_login.text == "Products", "Login Unsuccessful"

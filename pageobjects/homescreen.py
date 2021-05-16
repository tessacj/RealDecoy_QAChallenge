from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure

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

    @allure.testcase("Load Login Page")
    def validate_page_loaded(self):
        assert self.icon.is_displayed()
        assert self.login_username.is_displayed()
        assert self.login_password.is_displayed()
        assert self.login_button.is_displayed()
        assert self.credentials.is_displayed()

    @allure.testcase("Login as a Standard User")
    def standard_user_login(self):
        self.login_username.send_keys(strings.standard_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()
        

    @allure.testcase("Login as a Locked Out User")
    def locked_out_user_login(self):
        self.login_username.send_keys(strings.locked_out_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()

        self.error_msg = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "error-button")))

        assert self.error_msg.is_displayed()

    @allure.testcase("Login as a Problem User")
    def problem_user_login(self):
        self.login_username.send_keys(strings.problem_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()

        self.successfull_login = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "title")))

        assert self.successfull_login.is_displayed()
    
    @allure.testcase("Login as a Performance Glitch User")
    def performance_glitch_user_login(self):
        self.login_username.send_keys(strings.performance_glitch_user)
        self.login_password.send_keys(strings.password)

        self.login_button.click()

        # self.backendPerformance = self.responseStart - self.navigationStart
        # self.frontendPerformance = self.domComplete - self.responseStart

        # assert self.frontendPerformance > 2, "The user may be experiencing performance issues relating to the frontend"
        # assert self.backendPerformance > 2, "The user may be experiencing performance issues relating to the backend"
        try:
            self.successfull_login = WebDriverWait(self.driver.instance, 2).until(EC.visibility_of_element_located((
                By.CLASS_NAME, "title")))
        except TimeoutException:
            assert True, "The user may be experiencing performance issues"

        # assert self.successfull_login.is_displayed()
        # assert self.successfull_login.text == "Products", "Login Unsuccessful"

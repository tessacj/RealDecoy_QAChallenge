from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure

from values import strings


class SideBar:
    def __init__(self, driver):
        self.driver = driver

        self.menu_bar = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='react-burger-menu-btn']")))
    
    @allure.testcase("Open Menu Side Bar")
    def validate_component_elements(self):
        assert self.menu_bar.is_displayed()

    @allure.testcase("Click the All Items Option")
    def menu_item_all_items(self):
        self.menu_bar.click()
        self.all_items = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='inventory_sidebar_link']")))

        self.all_items.click()

    @allure.testcase("Click the About Option")
    def menu_item_about(self):
        self.menu_bar.click()
        self.about_item = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='about_sidebar_link']")))

        self.about_item.click()

    @allure.testcase("Click the Logout Option")
    def menu_item_logout(self):
        self.menu_bar.click()
        self.logout_item = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='logout_sidebar_link']")))

        self.logout_item.click()

    @allure.testcase("Click the Reset App State Option")
    def menu_item_reset_app_state(self):
        self.menu_bar.click()
        self.reset_app_item = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='reset_sidebar_link']")))

        self.reset_app_item.click()

        
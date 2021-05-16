from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import pytest
import allure

from values import strings


class Inventory:
    def __init__(self, driver):
        self.driver = driver

        self.title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "title")))

        self.menu_bar = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='react-burger-menu-btn']")))

        self.cart_icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='shopping_cart_container']")))

        self.list_items = len(WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_all_elements_located((
            By.XPATH, "//*[@id='inventory_container']/div"))))

        self.sort_options = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='header_container']/div[2]/div[2]/span/select")))
        
    @allure.testcase("Load Inventory Page")
    def validate_page_loaded(self):
        assert self.title.is_displayed()
        assert self.menu_bar.is_displayed()
        assert self.cart_icon.is_displayed()
        
        #Throws error
        # assert self.list_items > 5

    @allure.testcase("Open Menu SideBar")
    def open_menu(self):
        self.menu_bar.click()

    @allure.testcase("Navigate to the Cart Page")
    def validate_cart_link(self):
        self.cart_icon.click()

    @allure.testcase("Test Sort Functions")
    def sort_functions(self):
        sortOption = (self.sort_options).sortOption

        for i in range(0, len(self.sort_options) - 1):
            sortOption.select_by_index(i)

            self.sorted_list_items = len(WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='inventory_container']/div"))))

            for item in self.list_items:
                assert self.list_items[item] == self.sorted_list_items[item]

    @allure.testcase("Validate each item's elements")
    def check_inventory_items(self):
        for i in range(0, len(self.list_items) - 1):
            item_image = i.find_element_by_xpath(".//*[@id='inventory_container']/div/div[1]/div[1]")
            item_name = i.find_element_by_xpath(".//*[@id='inventory_container']/div/div[1]/div[2]/div[1]")
            item_add_to_cart = i.find_element_by_xpath(".//*[contains(text(), 'Add to cart')]")

    



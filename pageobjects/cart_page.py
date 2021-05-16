from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

from values import strings


class Cart:
    def __init__(self, driver):
        self.driver = driver

        self.cart_icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='shopping_cart_container']")))

    #Function to validate the cart page elements without adding an item to it
    @allure.testcase("Load Cart Page Without adding items")
    def navigate_to_cart_without_items(self):
        self.cart_icon.click()

        self.cart_page_title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "title")))

        assert self.cart_page_title.is_displayed()

        self.cart_list_items = len(WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_all_elements_located((
            By.XPATH, "//*[@id='cart_contents_container']/div/div[1]"))))

        assert self.cart_list_items <= 2, "Cart has more than 1 item added"

        self.cart_continue_shopping_btn = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, ".//*[contains(text(), 'Continue Shopping')]")))
        
        self.cart_continue_shopping_btn.is_displayed()

        self.cart_checkout_btn = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, ".//*[contains(text(), 'Checkout')]")))
        
        self.cart_checkout_btn.is_displayed()

    #Function to validate the cart page elements when an item is added to it
    @allure.testcase("Load Cart Page With items added")
    def navigate_to_cart_with_items(self):
        self.cart_add_item = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))

        self.cart_add_item.click()

        self.cart_icon.click()

        self.cart_page_title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "title")))

        self.cart_page_title.is_displayed()

        self.cart_list_items = len(WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_all_elements_located((
            By.XPATH, "//*[@id='cart_contents_container']/div/div[1]"))))

        assert self.cart_list_items > 2, "Item not added to cart"

        self.cart_continue_shopping_btn = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, ".//*[contains(text(), 'Continue Shopping')]")))
        
        self.cart_continue_shopping_btn.is_displayed()

        self.cart_checkout_btn = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((
            By.XPATH, ".//*[contains(text(), 'Checkout')]")))
        
        self.cart_checkout_btn.is_displayed()
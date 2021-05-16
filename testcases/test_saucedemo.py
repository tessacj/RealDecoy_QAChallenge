import unittest
from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen
from pageobjects.inventory_page import Inventory
from pageobjects.side_bar import SideBar
from pageobjects.footer import Footer
from pageobjects.cart_page import Cart


class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_page_loaded()
    
    def test_standard_user_login_function(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        inventory_page = Inventory(self.driver)
        inventory_page.validate_page_loaded()

    def test_locked_out_user_login_function(self):
        home_screen = HomeScreen(self.driver)
        home_screen.locked_out_user_login()
    
    def test_problem_user_login_function(self):
        home_screen = HomeScreen(self.driver)
        home_screen.problem_user_login()
    
    def test_performance_glitch_user_login_function(self):
        home_screen = HomeScreen(self.driver)
        home_screen.performance_glitch_user_login()

    def test_inventory_page_components_as_standard_user(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        inventory_page = Inventory(self.driver)
        inventory_page.validate_page_loaded()
        inventory_page.open_menu()
        inventory_page.validate_cart_link()
    
    def test_inventory_page_sort_functions(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        inventory_page = Inventory(self.driver)
        inventory_page.sort_functions()

    def test_footer_fb_link(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        footer = Footer(self.driver)
        footer.facebook_check()

    def test_footer_twitter_link(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        footer = Footer(self.driver)
        footer.twitter_check()
    
    def test_footer_linkedin_link(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        footer = Footer(self.driver)
        footer.linkedin_check()

    def test_sidebar_elements(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        sidebar = SideBar(self.driver)
        sidebar.validate_component_elements()

    def test_sidebar_all_items_link(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        sidebar = SideBar(self.driver)
        sidebar.menu_item_all_items()

    def test_sidebar_about_link(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        sidebar = SideBar(self.driver)
        sidebar.menu_item_about()
    
    def test_logout_function(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        sidebar = SideBar(self.driver)
        sidebar.menu_item_logout()
        home_screen.validate_page_loaded()
    
    def test_cart_page_without_items(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        cart_page = Cart(self.driver)
        cart_page.navigate_to_cart_without_items()

    def test_cart_page_with_items(self):
        home_screen = HomeScreen(self.driver)
        home_screen.standard_user_login()
        cart_page = Cart(self.driver)
        cart_page.navigate_to_cart_with_items()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()
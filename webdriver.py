from selenium import webdriver


class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome()

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
            self.instance.maximize_window()
        else:
            raise TypeError("URL must be a string.")
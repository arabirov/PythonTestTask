import unittest
import logging

from selenium import webdriver

from tests.Constants.paths import *
from tests.Pages.first_page import FirstPage  # Импорт классов Pages
from tests.Pages.second_page import SecondPage
from tests.Pages.third_page import ThirdPage

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Pages:
    def __init__(self, driver):
        self.driver = driver

        self.first_page = FirstPage(driver)
        self.second_page = SecondPage(driver)
        self.third_page = ThirdPage(driver)


class EnvironmentFirefox(unittest.TestCase, Pages):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, service_log_path=FIREFOX_DRIVER_LOGS_PATH)
        pages = Pages(cls.driver)
        cls.first_page = pages.first_page
        cls.second_page = pages.second_page
        cls.third_page = pages.third_page
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_FORM_URL)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

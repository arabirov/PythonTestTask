import unittest
import logging

from selenium import webdriver

from tests.Constants.paths import *
from tests.Pages.first_page import FirstPage  # Импорт классов Pages
from tests.Pages.second_page import SecondPage
from tests.Pages.third_page import ThirdPage

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class EnvironmentFirefox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, service_log_path=FIREFOX_DRIVER_LOGS_PATH)
        cls.first_page = FirstPage(cls.driver)
        cls.second_page = SecondPage(cls.driver)
        cls.third_page = ThirdPage(cls.driver)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_FORM_URL)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

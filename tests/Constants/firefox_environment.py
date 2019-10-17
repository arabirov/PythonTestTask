import unittest
import logging
import time
import datetime
import random

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.Constants.paths import *
from tests.Pages.first_page import FirstPage  # Импорт классов Pages
from tests.Pages.second_page import SecondPage
from tests.Pages.third_page import ThirdPage

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Env(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH, service_log_path=FIREFOX_DRIVER_LOGS_PATH)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_FORM_URL)
        cls.first_page = FirstPage(cls.driver)
        cls.second_page = SecondPage(cls.driver)
        cls.third_page = ThirdPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
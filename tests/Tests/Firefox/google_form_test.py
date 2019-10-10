from selenium import webdriver
from tests.Constants.paths import *
import unittest
import logging
import time
from tests.Pages.first_page import FirstPage  # Импорт классов Pages
from tests.Pages.second_page import SecondPage
from tests.Pages.third_page import ThirdPage

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class GoogleFormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH,
                                           service_log_path=DRIVER_LOGS_PATH + "/geckodriver.log")
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()
        cls.driver.get(GOOGLE_FORM_URL)

    def test_01_fill_first_and_second_questions(self):
        driver = self.driver
        first_page = FirstPage(driver)
        first_page.checkbox_list_parse("Check this")

    def test_02_validate_third_question_mandatory(self):
        driver = self.driver

    def test_03_fill_third_question_go_to_next_page(self):
        driver = self.driver

    def test_04_fill_questions_on_second_page(self):
        driver = self.driver

    def test_05_go_to_first_page(self):
        driver = self.driver

    def test_06_reverse_text_in_third_question(self):
        driver = self.driver

    def test_07_go_to_second_page(self):
        driver = self.driver

    def test_08_check_that_questions_are_filled(self):
        driver = self.driver

    def test_09_go_to_third_page(self):
        driver = self.driver

    def test_10_fill_question_and_send_form(self):
        driver = self.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()



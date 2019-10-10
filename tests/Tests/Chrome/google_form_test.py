from selenium import webdriver
from tests.Constants.paths import *
import unittest
from tests.Pages.first_page import FirstPage  # Импорт классов Pages
from tests.Pages.second_page import SecondPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,
                                           service_log_path=DRIVER_LOGS_PATH + "/chromedriver.log")
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_01_fill_first_and_second_questions(self):
        driver = self.driver

        login = FirstPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = SecondPage(driver)
        homepage.click_welcome()
        homepage.click_welcome()
        homepage.click_logout()

    # def test_02_validate_third_question_mandatory(self):
    #     driver = self.driver
    #
    # def test_03_fill_third_question_go_to_next_page(self):
    #     driver = self.driver
    #
    # def test_04_fill_questions_on_second_page(self):
    #     driver = self.driver
    #
    # def test_05_go_to_first_page(self):
    #     driver = self.driver
    #
    # def test_06_reverse_text_in_third_question(self):
    #     driver = self.driver
    #
    # def test_07_go_to_second_page(self):
    #     driver = self.driver
    #
    # def test_08_check_that_questions_are_filled(self):
    #     driver = self.driver
    #
    # def test_09_go_to_third_page(self):
    #     driver = self.driver
    #
    # def test_10_fill_question_and_send_form(self):
    #     driver = self.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()



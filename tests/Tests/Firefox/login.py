from selenium import webdriver
from tests.Constants.paths import *
import unittest
import sys
import argparse
from tests.Pages.FirstPage import LoginPage  # Импорт классов Pages
from tests.Pages.SecondPage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH,
                                           service_log_path=DRIVER_LOGS_PATH + "/geckodriver.log")
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    sys.argv.extend(['--browser', 'Chrome'])

    parser = argparse.ArgumentParser()
    parser.add_argument('--browser')
    args = parser.parse_args()
    sys.argv[0:] = args
    print(sys.argv)
    unittest.main()



from tests.Constants.locators import Locators
from tests.Pages.second_page import SecondPage
import time


class FirstPage:

    def __init__(self, driver):  # Создание конструктора класса
        self.driver = driver
        #
        # self.username_textbox_id = Locators.username_testbox_id  # Импорт объекта из класса Constants
        # self.password_textbox_id = "txtPassword"  # Добавление всех объектов на странице
        # self.login_button_textbox_id = "btnLogin"
        self.checkbox = Locators.FIRST_STEP_CHECKBOX  # Импорт объекта из класса Constants

    # def enter_username(self, username):  # добавление всех действий на странице
    #     self.driver.find_element_by_id(self.username_textbox_id).clear()
    #     self.driver.find_element_by_id(Locators.username_testbox_id).send_keys(username)  # Использование импортированного локатора, не лучшая практика
    #     return self
    #
    # def enter_password(self, password):
    #     self.driver.find_element_by_id(self.password_textbox_id).clear()
    #     self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    #     return self
    #
    # def click_login(self):
    #     self.driver.find_element_by_id(self.login_button_textbox_id).click()
    #     return SecondPage

    def checkbox_list_parse(self, text):
        amount = self.driver.find_elements_by_css_selector(self.checkbox).__len__()
        for element in self.driver.find_elements_by_css_selector(self.checkbox):
            # i = 0
            # if i < amount:
            if element.text == text:
                element.click()
                # i += 1

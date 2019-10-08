from tests.Constants.locators import Locators


class LoginPage:

    def __init__(self, driver):  # Создание конструктора класса
        self.driver = driver

        self.username_textbox_id = Locators.username_testbox_id  # Импорт объекта из класса Constants
        self.password_textbox_id = "txtPassword"  # Добавление всех объектов на странице
        self.login_button_textbox_id = "btnLogin"

    def enter_username(self, username):  # добавление всех действий на странице
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_testbox_id).send_keys(username)  # Использование импортированного локатора, не лучшая практика

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_textbox_id).click()

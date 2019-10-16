from tests.Constants.locators import Locators


class ThirdPage:

    def __init__(self, driver):  # Создание конструктора класса
        self.driver = driver

        self.__radio_buttons_array = Locators.RADIO_ARRAY
        self.__next_button = Locators.NEXT_BUTTON

    def radio_array(self):
        radio_array_ = self.driver.find_elements_by_css_selector(self.__radio_buttons_array)
        return radio_array_

    def radio_click(self, index):
        self.radio_array()[index].click()
        return self

    def next_button_click(self):
        self.driver.find_element_by_css_selector(self.__next_button).click()

from tests.Constants.locators import Locators


class SecondPage:
    def __init__(self, driver):
        self.driver = driver

        self.__movies_field = Locators.SECOND_STEP_MOVIES
        self.__check_radio_button = Locators.SECOND_STEP_RADIO_CHECK
        self.__radio_buttons_array = Locators.RADIO_ARRAY
        self.__back_button = Locators.BACK_BUTTON
        self.__next_button = Locators.NEXT_BUTTON

    def fill_movies_field(self, movies):
        self.driver.find_element_by_css_selector(self.__movies_field).send_keys(movies)
        return self

    def get_movies_field(self):
        movies = self.driver.find_element_by_css_selector(self.__movies_field).get_attribute("data-initial-value")
        return movies

    def radio_array(self):
        radio_array_ = self.driver.find_elements_by_css_selector(self.__radio_buttons_array)
        return radio_array_

    def radio_click(self, index):
        self.radio_array()[index].click()
        return self

    def back_button_click(self):
        self.driver.find_element_by_css_selector(self.__back_button).click()
        return self

    def next_button_click(self):
        self.driver.find_element_by_css_selector(self.__next_button).click()
        return self

    def check_radio_array(self):
        color = self.driver.find_element_by_css_selector(self.__check_radio_button).get_attribute("value")
        return color

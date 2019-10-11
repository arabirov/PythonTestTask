from tests.Constants.locators import Locators


class SecondPage:
    def __init__(self, driver):
        self.driver = driver

        self.__movies_field = Locators.SECOND_STEP_MOVIES
        self.__radio_buttons_array = Locators.SECOND_STEP_RADIO_CHECK

    def fill_movies_field(self, movies):
        self.driver.find_element_by_css_selector(self.__movies_field).send_keys(movies)
        return self

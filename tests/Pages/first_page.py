from tests.Constants.locators import Locators


class FirstPage:

    def __init__(self, driver):  # Создание конструктора класса
        self.driver = driver

        self.__checkbox_array = Locators.FIRST_STEP_CHECKBOX  # Импорт объекта из класса Locators
        self.__next_button = Locators.BACK_BUTTON
        self.__necessity_field = Locators.FIRST_STEP_CHECK_NECESSITY_FIELD
        self.__firefox_day_field = Locators.FIRST_STEP_FIREFOX_SET_DAY
        self.__firefox_month_field = Locators.FIRST_STEP_FIREFOX_SET_MONTH
        self.__firefox_year_field = Locators.FIRST_STEP_FIREFOX_SET_YEAR
        self.__current_month_field = Locators.FIRST_STEP_CURRENT_MONTH

    def checkbox_list_parse_and_click(self, text):  # добавление всех действий на странице
        for element in self.driver.find_elements_by_css_selector(self.__checkbox_array):
            if element.text == text:
                element.click()
        return self

    def next_button_click(self):
        self.driver.find_element_by_css_selector(self.__next_button).click()
        return self

    def check_necessity_field(self):
        return self.driver.find_element_by_css_selector(self.__necessity_field).is_displayed()

    def set_date_firefox(self, day, month, year):
        self.driver.find_element_by_css_selector(self.__firefox_day_field).send_keys(day)
        self.driver.find_element_by_css_selector(self.__firefox_month_field).send_keys(month)
        self.driver.find_element_by_css_selector(self.__firefox_year_field).send_keys(year)
        return self

    def set_current_month(self, month):
        self.driver.find_element_by_css_selector(self.__current_month_field).send_keys(month)
        return self

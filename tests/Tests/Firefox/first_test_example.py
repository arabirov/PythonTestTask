import datetime

from tests.Constants.firefox_environment import Pages


class FirstPage:

    def __init__(self, driver):
        self.driver = driver
        self.pages = Pages(driver)

    def test_01_fill_first_and_second_questions(self):
        first_page = self.pages.first_page
        i = 0
        for element in first_page.checkbox_list():
            if i < first_page.checkbox_list().__len__():
                if element.text == "Check this":
                    first_page.checkbox_click(i)
                i += 1
        plus_5_days = datetime.date.today() + datetime.timedelta(days=5)
        first_page.set_date_firefox(str(plus_5_days.day), str(plus_5_days.month), str(plus_5_days.year))
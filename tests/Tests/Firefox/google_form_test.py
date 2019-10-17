import unittest
import logging
import time
import datetime
import random

from tests.Constants.firefox_environment import Env, Pages

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_random_movies():
    movies = list()
    movies.append("High Rollers")
    movies.append("Apocalypse Now")
    movies.append("Fullmetal Alchemist: Brotherhood")
    movies.append("The Grand Budapest Hotel")
    movies.append("Pulp Fiction")
    movies.append("Trigun")
    movies.append("Snatch")
    movies.append("Knockin' on Heaven's Door")
    random_movies = set()
    while random_movies.__len__() < 3:
        random_movies.add(movies[random.randrange(movies.__len__())])
        if random_movies.__len__() >= 3:
            movies_list = "\n".join(random_movies)
            return movies_list


class GoogleFormTest(Env, Pages):

    def test_01_fill_first_and_second_questions(self):
        i = 0
        for element in self.first_page.checkbox_list():
            if i < self.first_page.checkbox_list().__len__():
                if element.text == "Check this":
                    self.first_page.checkbox_click(i)
                i += 1
        plus_5_days = datetime.date.today() + datetime.timedelta(days=5)
        self.first_page.set_date_firefox(str(plus_5_days.day), str(plus_5_days.month), str(plus_5_days.year))

    def test_02_validate_third_question_mandatory(self):
        self.first_page.next_button_click()
        if self.first_page.check_necessity_field():
            pass
        else:
            self.test_02_validate_third_question_mandatory()

    def test_03_fill_third_question_go_to_next_page(self):
        month = datetime.date.today().strftime("%B")
        self.first_page.set_current_month(month)
        time.sleep(1)
        self.first_page.next_button_click()

    def test_04_fill_questions_on_second_page(self):
        self.second_page.fill_movies_field(get_random_movies())
        i = 0
        for element in self.second_page.radio_array():
            if i < self.second_page.radio_array().__len__():
                if element.text == "Yellow":
                    self.second_page.radio_click(i)
                i += 1
        time.sleep(3)

    def test_05_go_to_first_page(self):
        self.second_page.back_button_click()

    def test_06_reverse_text_in_third_question(self):
        month_reversed = "".join(reversed(self.first_page.get_current_month()))
        self.first_page.set_current_month(month_reversed)
        time.sleep(3)

    def test_07_go_to_second_page(self):
        self.first_page.next_button_click()

    def test_08_check_that_questions_are_filled(self):
        self.assertNotEqual(self.second_page.get_movies_field(), "")
        self.assertEqual(self.second_page.check_radio_array(), "Yellow")

    def test_09_go_to_third_page(self):
        self.second_page.next_button_click()

    def test_10_fill_question_and_send_form(self):
        i = 0
        for element in self.third_page.radio_array():
            if i < self.third_page.radio_array().__len__():
                if element.text == "Yes":
                    self.third_page.radio_click(i)
                i += 1
        time.sleep(1)
        self.third_page.next_button_click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()

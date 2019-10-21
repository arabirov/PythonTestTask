import unittest
import logging
import argparse

from tests.Tests.Firefox.google_form_test import GoogleFormTest
from tests.Constants.firefox_environment import EnvironmentFirefox

logger = logging.getLogger()
logger.setLevel(logging.INFO)

browser_parse = argparse.ArgumentParser()
browser_parse.add_argument("-b", "--browser", required=True, help="Please, enter browser with -b/--browser key")
browser = vars(browser_parse.parse_args())
EnvironmentFirefox.browser = str(browser["browser"]).lower()

TestLoader = unittest.TestLoader()
suite = TestLoader.loadTestsFromTestCase(GoogleFormTest)
TestSuite = unittest.TestSuite()
TestSuite.addTest(suite)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)

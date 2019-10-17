import unittest
import logging

from tests.Tests.Firefox.google_form_test import GoogleFormTest

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TestLoader = unittest.TestLoader()
suite = TestLoader.loadTestsFromTestCase(GoogleFormTest)
TestSuite = unittest.TestSuite()
TestSuite.addTest(suite)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)

import os


FIREFOX_DRIVER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                           'resources/geckodriver')
CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                           'resources/chromedriver')
DRIVER_LOGS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                'logs/driver_logs')
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScNx9xK2LM-G3Z3fJXOQapiSK1IAoNXc_67MyS-soTfhDXotA/viewform"

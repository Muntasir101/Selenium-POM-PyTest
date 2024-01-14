
login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

BROWSER = 'firefox'

# config.py
import logging

# Logging configuration
import os
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOGGING_FILENAME = os.path.join(os.getcwd(),  'log', 'test.log')

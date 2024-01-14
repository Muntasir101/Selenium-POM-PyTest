import os

from POM.pages.login_page import LoginPage
from POM.data.login_data import LoginTestData
import logging
from POM.utils.config import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME


# Implement Logging interface
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

# Create a file handler and set the logging level
file_handler = logging.FileHandler(LOGGING_FILENAME)
file_handler.setLevel(LOGGING_LEVEL)

# Create a formatter and add it to the file handler
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


def test_login_valid(setup):
    logger.info("Starting the valid login test")
    login_page = LoginPage(setup)
    login_page.login(LoginTestData.VALID_USERNAME, LoginTestData.VALID_PASSWORD)
    logger.info(f"Enter Username: {LoginTestData.VALID_USERNAME}")
    logger.info(f"Enter Password: {LoginTestData.VALID_PASSWORD}")
    logger.info("Test Case Execution Completed.")
    login_page.driver.get_screenshot_as_file(os.path.join(os.getcwd(), 'Screenshots'+"\\Login_Valid.png"))
    logger.info("-----------End-----------")


def test_login_invalid(setup):
    logger.info("Starting the Invalid login test")
    login_page = LoginPage(setup)
    login_page.login(LoginTestData.INVALID_USERNAME, LoginTestData.INVALID_PASSWORD)
    logger.info(f"Enter Username: {LoginTestData.INVALID_USERNAME}")
    logger.info(f"Enter Password: {LoginTestData.INVALID_PASSWORD}")
    logger.info("Test Case Execution Completed.")
    login_page.driver.get_screenshot_as_file(os.path.join(os.getcwd(), 'Screenshots' + "\\Login_InValid.png"))
    logger.info("-----------End-----------")
    # Add assertions and further test steps

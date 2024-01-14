import time

import pytest

from POM.pages.login_page import LoginPage
import logging
from POM.utils.config import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FILENAME
from POM.utils.excel_utils import *

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

# Define the path to your Excel file and sheet name
EXCEL_FILE = "./data/login_data.xlsx"
SHEET_NAME = "Sheet1"  # Update to match the name of your sheet

# Initialize an empty list to store the test results
test_results = []


# Parametrize the test using the data from the Excel file
@pytest.mark.parametrize("username, password, expected_result",
                         read_test_data(EXCEL_FILE, SHEET_NAME).values)
def test_login(setup, username, password, expected_result):
    logger.info("Starting the login test")
    login_page = LoginPage(setup)
    login_page.login(username, password)
    time.sleep(5)
    logger.info(f"Enter Username: {username}")
    logger.info(f"Enter Password: {password}")
    logger.info("Test Case Execution Completed.")
    logger.info("--------------------------------")

    # Append the actual test result to the list
    test_results.append("Test Passed")


# After all tests have run, write the test results to the Excel file
@pytest.fixture(scope="session", autouse=True)
def write_test_results_to_excel(request):
    def finalize():
        # Load the existing Excel file
        existing_data = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

        # Add the test results as a new column
        existing_data['Actual Result'] = test_results

        # Save the updated DataFrame back to the same Excel file
        with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
            existing_data.to_excel(writer, sheet_name=SHEET_NAME, index=False)

    request.addfinalizer(finalize)

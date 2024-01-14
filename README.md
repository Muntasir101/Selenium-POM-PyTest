## Selenium Python Pytest Page Object Model (POM) Framework
# Overview
This project is a Selenium-based automation framework implemented in Python, utilizing the Pytest testing framework and following the Page Object Model (POM) design pattern. The framework aims to provide a scalable, maintainable, and efficient structure for writing automated tests for web applications.

# Prerequisites
1. Python 3.x
2. Pip (Python package installer)
3. Selenium WebDriver
4. Pytest

# Installation

# Clone Repository: 
git clone https://github.com/muntasir101/selenium-pytest-pom.git

# Navigate to the project directory:
cd selenium-pytest-pom

# Activate venv
1. pip install virtualenv
2. virtualenv venvironment
3. venvironment\Scripts\activate

# Install the required dependencies:
pip install -r requirements.txt

# Running Tests
pytest -v tests/test_login.py 

# Reporting: 
pytest .\tests\test_login_page_ddt.py --html-report=./Reports/Login_Report.html

Test execution reports will be generated in the reports folder. Open the HTML report in a web browser to view detailed test results.

# Contribution
Feel free to contribute to the project by submitting issues or pull requests. Follow the guidelines outlined in the CONTRIBUTING.md file.

import inspect

import pytest
import logging
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("invoke_browser")
class Base:
    def making_loop(self, itmes):
        for i in itmes:
            if i.text == "Patients":
                i.click()

    def select_dropdown(self, locator, index):
        Dropdown_list = Select(locator)
        Dropdown_list.select_by_index(index)

    def execute_java(self, locator):
        self.Driver.execute_script(locator)

    def logs_information(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        add_file = logging.FileHandler("logs_for_test.log")
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        add_file.setFormatter(log_format)

        logger.addHandler(add_file)

        return logger

    def get_screenshot(self, Driver):
        Driver.get_screenshot_as_file("screenshot.jpeg")
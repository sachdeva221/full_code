import pytest
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

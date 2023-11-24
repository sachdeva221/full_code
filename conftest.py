import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--name", action="store", default="firefox"
    )




@pytest.fixture(scope="class")
def invoke_browser(request):
    global Driver
    browser_name = request.config.getoption("name")
    if browser_name == "chrome":
        Driver = webdriver.Chrome()
        Driver.maximize_window()

    elif browser_name == "firefox":
        Driver = webdriver.Firefox()
        Driver.maximize_window()

    else:
        print("please enter the right name")
    Driver.implicitly_wait(15)
    request.cls.Driver = Driver
    yield
    Driver.close()





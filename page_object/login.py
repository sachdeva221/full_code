from selenium.webdriver.common.by import By

from page_object.patient import Patient


class First_page:
    def __init__(self, Driver):
        self.Driver = Driver

    url = "https://stage-admin.myintellispine.com"
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    btn = (By.CSS_SELECTOR, 'button[class="btn btn-primary w-full"]')

    def invoke_url(self):
        return self.Driver.get(First_page.url)

    def enter_email(self):
        return self.Driver.find_element(*First_page.email)

    def enter_password(self):
        return self.Driver.find_element(*First_page.password)

    def enter_login_btn(self):
        self.Driver.find_element(*First_page.btn).click()
        obj_const = Patient(self.Driver)
        return obj_const


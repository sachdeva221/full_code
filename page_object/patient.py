from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Base import Base


class Patient(Base):
    def __init__(self, Driver):
        self.Driver = Driver

    item_list = (By.CSS_SELECTOR, 'a[class="nav-link"]')
    new_patient = (By.CSS_SELECTOR, 'a[class="btn btn-primary"]')
    drop_options = (By.NAME, "salutation")
    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")
    phone_number = (By.CSS_SELECTOR, 'input[class="form-control"]')
    date_picker = (By.CSS_SELECTOR, 'input[class="form-control"]')
    p_email = (By.ID, "email")
    address = (By.NAME, "address")
    zipcode = (By.NAME, "zipcode")
    city = (By.NAME, "city")
    save = (By.CSS_SELECTOR, 'button[class="btn btn-primary w-sm-40]"')



    def menu(self):
        self.list_itmes = self.Driver.find_elements(*Patient.item_list)
        return self.making_loop(self.list_itmes)

    def click_add_patient(self):
        return self.Driver.find_element(*Patient.new_patient)

    def select_title(self):
        Dropdown = self.Driver.find_element(*Patient.drop_options)
        return self.select_dropdown(Dropdown, 1)

    def fill_firstname(self):
        return self.Driver.find_element(*Patient.firstname)

    def fill_lastname(self):
        return self.Driver.find_element(*Patient.lastname)

    def fill_number(self):
        return self.Driver.find_element(*Patient.phone_number)

    def select_date(self):
        date_input = self.Driver.find_element(*Patient.date_picker)
        date_to_set = "2023-10-17"
        return self.Driver.execute_script(f"arguments[0].value = '{date_to_set}';", date_input)

    def enter_mail(self):
        return self.Driver.find_element(*Patient.p_email)

    def enter_add(self):
        return self.Driver.find_element(*Patient.address)

    def enter_zipcode(self):
        return self.Driver.find_element(*Patient.zipcode)

    def enter_city(self):
        return self.Driver.find_element(*Patient.city)

    def click_save(self):
        return self.Driver.find_element(*Patient.save)

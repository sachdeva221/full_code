import time

import pytest

from Base import Base
from data_list import data_send_homepage
from page_object.login import First_page


class Test_runcode(Base):
    def test_run_file(self, get_data):
        obj = First_page(self.Driver)
        obj.invoke_url()
        time.sleep(2)
        obj.enter_email().send_keys(get_data[0])
        obj.enter_password().send_keys(get_data[1])
        list_item = obj.enter_login_btn()
        time.sleep(2)
        list_item.menu()
        time.sleep(2)
        list_item.click_add_patient().click()
        list_item.select_title()
        list_item.fill_firstname().send_keys(get_data[2])
        list_item.fill_lastname().send_keys(get_data[3])
        time.sleep(1)
        list_item.select_date()
        list_item.fill_number().send_keys(get_data[4])
        list_item.enter_mail().send_keys(get_data[5])
        list_item.enter_add().send_keys(get_data[6])
        list_item.enter_zipcode().send_keys(get_data[7])
        list_item.enter_city().send_keys(get_data[8])
        list_item.click_save().click()

    @pytest.fixture(params=data_send_homepage.list_info)
    def get_data(self, request):
        return request.param
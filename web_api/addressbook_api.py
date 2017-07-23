from selenium import webdriver

from web_api.group_helper import GroupHelper
from web_api.session_helper import SessionHelper

class AddressBook:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(1)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def message(self):
        return self.wd.find_element_by_xpath("//*[@id='content']/div").text

    def open_main_page(self):
        # Open main page
        self.wd.get(self.base_url)

    def is_element_present(self, by, value):
        return len(self.wd.find_elements(by, value)) != 0







    def return_group_page(self):
        # Return group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()



    def modify_group(self, index, group):
        wd = self.wd
        checkbox_edit_button = wd.find_elements_by_name("selected[]")
        checkbox_edit_button[index].click()
        edit_button = wd.find_element_by_xpath("//*[@id='content']/form/input[9]")
        edit_button.click()
        groupname_field = wd.find_element_by_xpath("//*[@id='content']/form/textarea[1]")
        groupname_field.clear()
        edit = wd.find_element_by_xpath("//*[@id='content']/form/input[3]")
        edit.click()


    def open_group_page(self):
        # Open group page
        wd =self.wd
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[3]/a").click()




    def destroy(self):
        self.wd.quit()
from selenium.webdriver.common.by import By
import time

class GroupHelper:
    def __init__(self, app):
        self.app = app
        pass
    def count(self):
        self.app.open_group_page()
        return len(self.app.wd.find_elements_by_name(("selected[]")))

    def is_present(self):
        self.app.open_group_page()
        return self.app.is_element_present(By.NAME, "selected[]")
    def create(self, group):
        # Create a group
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            # if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[12]").is_selected():
            #     wd.find_element_by_xpath("//div[@id='content']/form/select//option[12]").click()
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()

            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def delete(self, index):
        wd = self.app.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[index].click()
        if not checkboxes[index].is_selected():
            checkboxes[index].click()
        wd.find_element_by_name("delete").click()

    def delete_all(self):
        wd = self.app.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        for c in checkboxes:
            c.click()
        wd.find_element_by_name("delete").click()


    def modify(self, index, group):
        wd = self.app.wd
        checkbox_edit_button = wd.find_element_by_name("selected[]")
        checkbox_edit_button[index].click()
        time.sleep(5)
        edit_button = wd.find_element_by_xpath("//*[@id='content']/form/input[14]")
        edit_button.click()
        groupname_field = wd.find_element_by_xpath("//*[@id='content']/form/textarea[1]")
        groupname_field.clear()
        edit = wd.find_element_by_xpath("//*[@id='content']/form/input[3]")
        edit.click()

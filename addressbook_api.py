from selenium import webdriver
from selenium.webdriver.common.by import By

class AddressBook:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(10)
        self.base_url = base_url
    def message(self):
        return self.wd.find_element_by_xpath("//*[@id='content']/div").text

    def open_main_page(self):
        # Open main page
        self.wd.get(self.base_url)

    def is_element_present(self, by, value):
        return len(self.wd.find_elements(by, value)) != 0


    def is_logged(self):
        return self.is_element_present(By.NAME, "logout")

    def group_count(self):
        self.open_group_page()
        return len(self.wd.find_elements_by_name(("selected[]")))

    def is_group_present(self):
        self.open_group_page()
        return self.is_element_present(By.NAME, "selected[]")
    def login(self, user_name, password):
        # Fill form login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # Submit login
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        # Log Out
        wd = self.wd
        wd.find_element_by_xpath("//*[@id='top']/form/a").click()

    def return_group_page(self):
        # Return group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        # Create a group
        wd = self.wd
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



    def delete_group(self, index):
        wd = self.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[index].click()
        if not checkboxes[index] .is_selected():
            checkboxes[index].click()
        wd.find_element_by_name("delete").click()

    def delete_allgroups(self):
        wd = self.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        for c in checkboxes:
            c.click()
        wd.find_element_by_name("delete").click()

    def open_group_page(self):
        # Open group page
        wd =self.wd
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[3]/a").click()




    def destroy(self):
        self.wd.quit()
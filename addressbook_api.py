from selenium import webdriver
class AddressBook:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select//option[12]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()

        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        # Open group page
        wd =self.wd
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[3]/a").click()

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

    def open_main_page(self):
        # Open main page
        self.wd.get("http://localhost/addressbook/")
    def destroy(self):
        self.wd.quit()
from selenium import webdriver
import time, unittest


class test_create_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_test_create_group(self):
        wd = self.wd
        # Open main page
        wd.get("http://localhost/addressbook/")
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # Open group page
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[3]/a").click()
        # Create a group
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("My group")
        wd.find_element_by_name("group_header").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select//option[12]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Hello")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Hi")
        wd.find_element_by_name("submit").click()
        # TODO: Verify message about success
        # Return group page
        wd.find_element_by_link_text("group page").click()
        # Log Out
        wd.find_element_by_xpath("//*[@id='top']/form/a").click()
      # TODO: Verify group creation
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

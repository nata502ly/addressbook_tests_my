from addressbook_api import AddressBook
from models.group import Group
import time, unittest


class test_create_group(unittest.TestCase):
    def setUp(self):
        self.app = AddressBook()
    
    def test_test_create_group(self):
        group = Group("My group", "ddbdb", "Hi")
        self.app.open_main_page()
        self.app.login("admin", "secret")
        self.app.open_group_page()
        self.app.create_group(group)
        # TODO: Verify message about success
        self.app.return_group_page()
        self.app.logout()
      # TODO: Verify group creation



    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()

import pytest
from addressbook_api import AddressBook
from models.group import Group
from data.groups_data import groups_list
@pytest.fixture(scope="session")
def app():
    app = AddressBook()
    app.open_main_page()
    yield app
    app.destroy()

@pytest.fixture()
def init_login(app):
    if not app.is_logged():
        app.login("admin", "secret")
    yield
    # app.logout()
@pytest.fixture()
def init_groups(app):
    if not app.is_group_present():
        app.create_group(Group(name="Test"))
# my_file = open("some.json")
# groups = []
# for group in groups:
#     group.read()
# my_file.close()
# groups = [
# Group("My group", "ddbdb", "Hi")
# ]
@pytest.fixture()
def init_modify(app):
    app.modify_group(surname="Yuriivna")

@pytest.fixture(params=groups_list, ids=[str(g) for g in groups_list])
def group(request):
    return request.param
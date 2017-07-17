import pytest
import json
import os.path
from addressbook_api import AddressBook
from models.group import Group
from data.groups_data import groups_list

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json")

@pytest.fixture(scope="session")
def config(request):
    file_name= request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.load(f)

@pytest.fixture()
def app(selenium, config):
    app = AddressBook(selenium, base_url=config["base_url"])
    app.open_main_page()
    yield app
    app.destroy()

@pytest.fixture()
def init_login(app, config):
    if not app.is_logged():
        app.login(config["username"], config["password"])
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
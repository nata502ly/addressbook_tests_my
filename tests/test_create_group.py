import pytest

from models.group import Group



    
def test_create_group(app, init_login, group, db):
    with pytest.allure.step("GIVEN a group list"):
        old_group_list = db.get_group_list()
    with pytest.allure.step("WHEN I add the group{}".format(test_create_group)):
        app.open_main_page()
        app.open_group_page()
        app.group.create(group)
    with pytest.allure.step("THEN the success message appears"):
        assert "A new group has been entered into the address book." in app.message()
    app.return_group_page()

    with pytest.allure.step("THEN the new group list is equal to the old list with new added group"):
        new_group_list = db.get_group_list()
        assert len(old_group_list) + 1 == len(new_group_list)
        old_group_list.append(group)
        assert sorted(old_group_list) == sorted(new_group_list)
    # old_group_list.sort()
    # new_group_list.sort()
    # assert old_group_list == new_group_list



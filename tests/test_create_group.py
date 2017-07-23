
from models.group import Group



    
def test_create_group(app, init_login, group, db):
    old_group_list = db.get_group_list()
    app.open_main_page()
    app.open_group_page()
    app.group.create(group)
    # TODO: Verify message about success
    assert "A new group has been entered into the address book." in app.message()
    app.return_group_page()

  # TODO: Verify group creation
    new_group_list = db.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(old_group_list) == sorted(new_group_list)
    # old_group_list.sort()
    # new_group_list.sort()
    # assert old_group_list == new_group_list



import random
from models.group import Group


def test_delete_group(app, init_login, init_groups, db, group):
    old_group_list = db.get_group_list()
    index = random.randrange(app.group.count())

    app.open_group_page()
    app.group.delete(index)
    # TODO: Verify message about success
    assert "Group has been removed." in app.message()
    app.return_group_page()
    #TODO: Verify group deletion
    new_group_list = db.get_group_list()
    assert len(old_group_list)  == len(new_group_list) + 1
    # old_group_list.append(group)
    # assert sorted(old_group_list) == sorted(new_group_list)
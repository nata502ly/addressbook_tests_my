from models.group import Group
import random



def test_modify_group(app, init_login, init_groups, group):
    index = random.randrange(app.group_count())
    data_for_changing = Group(group.name)
    app.open_group_page()
    app.modify_group(index, data_for_changing)
    assert "Group record has been updated." in app.message()
    app.return_group_page()

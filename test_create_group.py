
from models.group import Group



    
def test_create_group(app, init_login, group):
    app.open_main_page()
    app.open_group_page()
    app.create_group(group)
    # TODO: Verify message about success
    assert "A new group has been entered into the address book." in app.message()
    app.return_group_page()

  # TODO: Verify group creation




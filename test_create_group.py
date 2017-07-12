
from models.group import Group



    
def test_create_group(app):
    group = Group("My group", "ddbdb", "Hi")
    app.open_main_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(group)
    # TODO: Verify message about success
    assert "A new group has been entered jjhj into the address book." in app.message()
    app.return_group_page()
    app.logout()
  # TODO: Verify group creation




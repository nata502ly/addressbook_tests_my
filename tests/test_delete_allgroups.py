def test_delete_group(app, init_login, init_groups):
    app.open_group_page()
    app.delete_allgroups()
    assert "Group has been removed." in app.message()
    app.return_group_page()
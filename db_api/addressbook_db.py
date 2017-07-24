import pymysql
from models.group import Group

class AddressbookDB:
    def __init__(self, **dbconfig):
        self. connection = pymysql.connect(**dbconfig, cursorclass=pymysql.cursors.DictCursor)

    def get_group_list(self):
        with self.connection.cursor() as cursor:
            sql = """SELECT group_id, group_name, group_header, group_footer FROM group_list ORDER BY group_name, group_id;
                  """
            cursor.execute(sql)
            result = []
            for row in cursor:
                result.append(Group(id=row["group_id"], name=row["group_name"], header = row["group_header"], footer = row["group_footer"]))
        self.connection.commit()
        return result
    def close(self):
        self.connection.close()

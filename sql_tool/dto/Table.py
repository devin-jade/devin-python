class Table(object):  # 类对象

    tableName = ''
    tableComment = ''
    fieldColumns = []

    def __init__(self, table_name, table_comment):
        self.tableName = table_name
        self.tableComment = table_comment
        self.fieldColumns = []

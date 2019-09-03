class TableColumn:  # 类对象

    fieldName = ''
    fieldType = ''
    fieldIndex = ''
    fieldNullAble = ''
    fieldDefault = ''
    fieldComments = ''
    fieldPrimaryKey = ''
    fieldUnique = ''

    def __init__(self, field_name, field_type, field_index, field_nullable, field_default, field_comments,
                 field_primary_key, field_unique):
        self.fieldName = field_name
        self.fieldType = field_type
        self.fieldIndex = field_index
        self.fieldNullAble = field_nullable
        self.fieldDefault = field_default
        self.fieldComments = field_comments
        self.fieldPrimaryKey = field_primary_key
        self.fieldUnique = field_unique

from sql_tool.dto.Table import *
from sql_tool.dto.TableColumn import *


def create_sql(table):
    sql = 'CREATE TABLE `' + table.tableName + '` ( \n'
    pri_key = None
    index_keys = []
    unique_index_keys = []
    for table_col in table.fieldColumns:
        sql = sql + '  `' + table_col.fieldName.lower() + '` ' + table_col.fieldType.lower()
        if table_col.fieldNullAble != 'Y':
            sql = sql + ' NOT NULL'
            if table_col.fieldDefault:
                sql = sql + ' DEFAULT ' + table_col.fieldDefault
            else:
                if 'varchar' in table_col.fieldType.lower():
                    sql = sql + ' DEFAULT ' + '\'\''
                if 'tinyint' in table_col.fieldType.lower():
                    sql = sql + ' DEFAULT ' + '0'
                if 'decimal' in table_col.fieldType.lower():
                    sql = sql + ' DEFAULT ' + '0.00'
                if 'datetime' in table_col.fieldType.lower():
                    sql = sql + ' DEFAULT ' + 'CURRENT_TIMESTAMP(6)'
            if table_col.fieldUnique == 'Y':
                sql = sql + 'UNIQUE'
        else:
            sql = sql + ' NULL    DEFAULT NULL'
        sql = sql + ' COMMENT ' + '\'' + table_col.fieldComments + '\'' + ',\n'
        if table_col.fieldPrimaryKey == 'Y':
            pri_key = table_col.fieldName
        if table_col.fieldIndex == 'Y':
            if table_col.fieldUnique == 'Y':
                unique_index_keys.append(table_col.fieldName)
            elif table_col.fieldPrimaryKey != 'Y':
                index_keys.append(table_col.fieldName)
    sql = sql + 'PRIMARY KEY (`' + pri_key + '`),\n'
    sql = sql + 'INDEX `pk_idx_' + pri_key + '` (`' + pri_key + '`),\n'
    for uk_idx in unique_index_keys:
        sql = sql + 'INDEX `idx_' + uk_idx + '` (`' + uk_idx + '`),\n'
    for idx in index_keys:
        sql = sql + 'INDEX `idx_' + idx + '` (`' + idx + '`),\n'
    sql = sql[:-2] + '\n'
    sql = sql + ') \n' + 'COMMENT ' + '\'' + table.tableComment + '\'\n'
    sql = sql + 'COLLATE = ' + '\'utf8mb4_general_ci\'\n' + 'ENGINE = InnoDB; \n'
    return sql

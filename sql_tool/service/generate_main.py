from sql_tool.service.generate_sql import *
from sql_tool.service.parse_sql_excel import *

if __name__ == "__main__":
    tables = read_excel("C:\\Users\\hp-430G5\\Desktop\\支付系统\\table\\t_thirdparty_interface.xlsx")
    print("tables is ", tables)
    tables_objs = build_table_obj(tables)
    print("table objs is ", tables_objs)
    for tables_obj in tables_objs:
        print("sql is ", create_sql(tables_obj))

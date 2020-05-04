import pymysql  # 导入数据库驱动程序模块
import sys  # 导入sys模块
try:
    conn = pymysql.connect(host='localhost', user='root',
                           password='123456A', db='py_database', port=3306, charset='utf8')
except:
    print('数据库连接出现错误，请重试')
    conn.close()
    sys.exit()
# ===============================数据库的CRUD操作
cur = conn.cursor()  # 创建游标实例
insert_sql = "insert into userinfo values('bd_test','12345678')"  # 插入数据操作
insert_sql1 = "insert into userinfo values('oukou','34567980')"
try:
    cur.execute(insert_sql)
    cur.execute(insert_sql1)
    conn.commit()
    print('插入数据成功')  # 插入数据成功
except:
    print('插入数据失败')
    conn.close()
    sys.exit()
# 更新数据
update_sql = "update userinfo set username= 'Elliot' where password = '654321'"
try:
    cur.execute(update_sql)
    conn.commit()
    print('更新数据成功')  # 更新数据成功
except:
    print('更新数据失败')
    conn.close()
    sys.exit()
# 删除数据
delete_sql = "delete from userinfo where password = '34567980'"
try:
    cur.execute(delete_sql)
    conn.commit()
    print('删除数据成功')  # 删除数据成功
except:
    print('删除数据失败')
    conn.close()
    sys.exit()
# 查询数据
select_sql = "select * from userinfo"
cur.execute(select_sql)
list_data = []
for i in cur.fetchall():
    list_data.append(i)
print(list_data) # [('Elliot', '654321'), ('bd_test', '12345678')]

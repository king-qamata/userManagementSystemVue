# Create your tests here.

import sqlite3

conn = sqlite3.connect('../userManagement.db')  # 连接数据库
cur = conn.cursor()  # 创建游标
# cur.execute(
#     "CREATE TABLE userData (date VARCHAR (20), name VARCHAR (20), tel VARCHAR (20), addr VARCHAR (20), desc VARCHAR (20))")
# data = ('2000-1-1','phase', '7789878799', '大版', 'sscsacascascsacsa')
# cur.execute('INSERT INTO userData (date, name, tel, addr, desc) VALUES (?, ?, ?, ?, ?)', data)
name ="tom"
print("DELETE FROM userData WHERE name = '{}'".format(name))
cur.execute("UPDATE userData SET date='{0}', tel='{1}', addr='{2}', desc='{3}' WHERE name = '{4}'".format('1111-11-11', '13704336865', '义乌', '实时', 'phase'))
# cur.execute("DELETE FROM userData WHERE name = '{}'".format(name))
# data = list()
# item_dict = dict()
# for item in cur.fetchall():
#     item_dict['date'] = item[0]
#     item_dict['name'] = item[1]
#     item_dict['tel'] = item[2]
#     item_dict['addr'] = item[3]
#     item_dict['desc'] = item[4]
#     data.append(item_dict)
conn.commit()  # 提交事务
cur.close()
conn.close()  # 关闭连接

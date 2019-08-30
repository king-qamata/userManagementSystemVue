# Create your views here.
from django.http import HttpResponse
import sqlite3
import json
import copy
import xlrd

def get_list(request):
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标
    cur.execute('select * from userData')

    data = list()
    item_dict = dict()
    for item in cur.fetchall():
        item_dict['date'] = item[0]
        item_dict['name'] = item[1]
        item_dict['tel'] = item[2]
        item_dict['addr'] = item[3]
        item_dict['desc'] = item[4]
        data.append(copy.deepcopy(item_dict))
    ret = HttpResponse(json.dumps(data))
    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def remove_user(request):
    req = request.GET
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标

    cur.execute("DELETE FROM userData WHERE name = '{}'".format(req['name']))
    ret = HttpResponse("success")

    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def edit_user(request):
    req = request.GET
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标

    cur.execute(
        "UPDATE userData SET date='{0}', tel='{1}', addr='{2}', desc='{3}' WHERE name = '{4}'"
            .format(req['date'], req['tel'], req['addr'], req['desc'], req['name']))

    ret = HttpResponse("success")

    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def add_user(request):
    req = request.GET
    conn = sqlite3.connect('userManagement.db')  # 连接数据库
    cur = conn.cursor()  # 创建游标
    cur.execute('INSERT INTO userData (date, name, tel, addr, desc) VALUES (?, ?, ?, ?, ?)',
                (req['date'], req['name'], req['tel'], req['addr'], req['desc']))

    conn.commit()  # 提交事务
    cur.close()
    conn.close()  # 关闭连接
    ret = HttpResponse('success')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret


def upload(request):
    print(request.method)
    print(request.path)
    print(type(request.POST))
    for k, v in dict(request.POST).items():
        print(k, v)
    with open('./1.jpg', 'wb+') as f:
        f.write(request.FILES.get('file').read())
    ret = HttpResponse('success')
    # 允许http://127.0.0.1:8001域向我发请求
    ret['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    if request.method == 'OPTIONS':
        # 所有的头信息都允许
        ret['Access-Control-Allow-Headers'] = '*'

    return ret

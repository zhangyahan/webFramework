from wsgiref.simple_server import make_server
from jinja2 import Template


# 将不同的内容部分封装成函数
def index(url):
    with open('./01_.html', 'r') as f:
        data = f.read()
    template = Template(data)  # 生成模板对象
    # 从数据库取出消息
    import pymysql

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='zyh1',
        password='zyh1997',
        database='demo1',
        charset='utf-8'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select * from table')
    ret = cursor.fetchall()
    print(ret)

    ret = template.render({'name': '张雅涵', 'hobby_list': ['烫头', '抽烟', '喝酒']})  # 把数据填充到模板中
    return ret.encode('utf-8')

def home(url):
    response = '家'.encode('utf-8')
    return response

fun_list = [
    ('/', index),
    ('home', home),
]

def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8',)])
    url = environ['PATH_INFO']
    func = None
    for i in fun_list:
        if url == i[0]:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b'not page'
    
    return [response,]


if __name__ == "__main__":
    httpd = make_server('127.0.0.1', 8090, run_server)  # 创建一个实例,执行函数和IP_PORT
    print('我在8090等你')
    httpd.serve_forever()  # 启动

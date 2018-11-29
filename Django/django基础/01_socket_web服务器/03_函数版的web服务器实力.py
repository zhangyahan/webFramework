"""
不完善的web服务器实例
"""

from socket import *

# 生成socket实例对象
sk = socket(AF_INET, SOCK_STREAM)
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定IP和端口
sk.bind(('127.0.0.1', 8000))
# 监听
sk.listen(10)


def index():
    response = '''
              <h1>主页</h1>
              <a href='/login'>登录</a>
              <a href='/register'>注册</a>
              '''
    return bytes(response, encoding='utf-8')

def login():
    with open('./index.html', 'rb') as f:
        response = f.read()
        return response


def register():
    response = '<h1>注册页</h1>'
    return bytes(response, encoding='utf-8')

def notPage(url):
    response = 'Not Page'
    return bytes(response, encoding='utf-8')

func_dict = [
    ('/', index),
    ('/login', login),
    ('/register', register),
]

# 写一个死循环,一直等待客户端连接
while 1:
    # 获取与客户段的连接
    conn, _ = sk.accept()
    # 接收客户端
    data = conn.recv(1024)
    url = data.decode('utf-8').split('\r\n')[0].split(' ')[1]
    print(url)
    # GET / HTTP/1.1\r\n  <-----------请求行
    # Host: 127.0.0.1:8000\r\n  <-------请求体
    # User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0\r\n
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
    # Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\n
    # Accept-Encoding: gzip, deflate\r\n
    # Connection: keep-alive\r\n
    # Upgrade-Insecure-Requests: 1\r\n
    # Cache-Control: max-age=0\r\n
    # \r\n <----------------空行
    # 请求方法 路径 版本协议\r\n
    # 请求体
    # 空行
    # 请求数据
    for i in func_dict:
        if i[0] == url:
            func = i[1]
            break
        else:
            notPage(url)
    # 发送消息
    # 版本协议 状态码 状态描述符\r\n
    # 响应体
    # \r\n
    # 响应正文
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    # 想让浏览器在页面上显示出来的内容都是响应正文
    response = func()
    conn.send(response)
    # 关闭
    conn.close()

sk.close()

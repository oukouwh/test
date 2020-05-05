from http.server import *
class request_handler(BaseHTTPRequestHandler):
    page = '''
        <html>
        <body>
        <p>hello,python</p>
        </body>
        </html>
    '''
    def do_GET(self): # 重写父类do_GET方法
        self.send_response(200) # 返回响应码
        self.protocol_version="HTTP/1.1" # 指定HTTP协议版本
        self.send_header("Content-Type","text/html") # 浏览器返回内容的格式
        self.send_header("Content-Length",str(len(self.page))) # 返回给浏览器的内容
        self.end_headers() # 相应头结束
        self.wfile.write(self.page.encode('utf-8')) # 字节流形式返回浏览器端
if __name__ == '__main__':
    serverAddress = ('127.0.0.1',8000) # 指定服务器ip地址和端口号
    server=HTTPServer(serverAddress,request_handler) # 创建web服务器实例
    server.serve_forever() # 持久性的执行web服务器

# 启动完成之后打开浏览器输入 http://127.0.0.1:8000/查看是否成功
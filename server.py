import http.server
import socketserver

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # 尝试获取请求的文件
            f = self.send_head()
            if f:
                self.copyfile(f, self.wfile)
                f.close()
        except FileNotFoundError:
            # 如果文件不存在，返回404页面
            self.send_error(404, "File not found")
            error_page = open("404.html", "rb")
            self.copyfile(error_page, self.wfile)
            error_page.close()

PORT = 80

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://0.0.0.0:{PORT}")
    print("Please visit http://192.168.1.104" )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


from http.server import HTTPServer, CGIHTTPRequestHandler

# 端口号
port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port：" + str(httpd.server_port))
httpd.serve_forever()


#    https://localhost:4442/web-camera/
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer


class CreateServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/web-camera/':
            self.path = '/index.html'
        try:
            file_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_open, 'utf-8'))

httpd = HTTPServer(('localhost', 4442), CreateServer)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()

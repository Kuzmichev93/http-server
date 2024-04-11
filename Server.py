import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

from Respons import Respons
from Parser import  Parser


class My(BaseHTTPRequestHandler,Respons):
    def do_GET(self):
        print(self.path)
        if self.path=='/decod':
            path = self.path.strip('/')
            data = open(path+".html",encoding="utf-8")
            text = data.read()
            data.close()
            self.send_response(200)
            self.send_header("Content-type",'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(text,'utf-8'))

        elif self.path == '/style.css':
            data = open(self.path.strip('/'),encoding="utf-8")
            text = data.read()
            self.send_response(200)
            self.send_header("Content-type",'text/css;')
            self.end_headers()
            self.wfile.write(bytes(text,'utf-8'))

        elif self.path == '/action.js':
            data = open(self.path.strip('/'),encoding="utf-8")
            text = data.read()
            self.send_response(200)
            self.send_header("Content-type",'text/js;')
            self.end_headers()
            self.wfile.write(bytes(text,'utf-8'))
        else:
            self.send_error(404,'Not found')

    def do_POST(self):
        if self.path=='/decod':
            data = int(self.headers["Content-Length"])
            resp = self.rfile.read(data)
            self.get_body = self.body(resp)

            if self.get_body['key'] == 'param':
                print(self.get_body['param'])
                send_value = Parser().get_respons(self.get_body['param'])
                self.send_response(200)
                self.send_header("Content-type",'application/json')
                self.end_headers()
                self.wfile.write(bytes(send_value,'utf-8'))
            else:
                self.send_error(404,'error parametr')
        else:
            self.send_error(404,'Not found')

def run(server_class=HTTPServer, handler_class=My):
    server_address = ('', 8060)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()



run()
from http.server import BaseHTTPRequesrHandler, HTTPServer
import random

class RequestHandler_httpd(BaseHTTPRequesrHandler):
	def do_GET(self):
		messagetosend = bytes((str((random.randint(1,100)))), "utf")
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
		self.send_header('Content-Length', len(messagetosend))
		self.end_header()
		self.wfile.write(messagetosend)
		return

server_address_httpd = ('192.168.66.19', 8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('start')
httpd.serve_forever()
from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class RequestHandler_httpd(BaseHTTPRequestHandler):
	def do_GET(self):
		global Request
		messagetosend = bytes('test', "utf")
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
		self.send_header('Content-Length', len(messagetosend))
		self.end_headers()
		self.wfile.write(messagetosend)
		Request = self.requestline
		Request = Request[5: int(len(Request)-9)]
		print(Request)
		return

server_address_httpd = ('192.168.66.19', 8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('start')
httpd.serve_forever()
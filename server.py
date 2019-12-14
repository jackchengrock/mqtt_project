from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import os

class RequestHandler_httpd(BaseHTTPRequestHandler):
	def fun():
		os.system("python3 project.py")

	def do_GET(self):
		global Request, test
		messagetosend = bytes('test', "utf")
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
		self.send_header('Content-Length', len(messagetosend))
		self.end_headers()
		self.wfile.write(messagetosend)
		Request = self.requestline
		Request = Request[5: int(len(Request)-9)]

		if Request[0:2] == 's1':
			print('head')
			os.system("python3 project.py")
		if Request[0:2] == 's2':
			print('QRcode')
		if Request[0:6] == 'state1':
			print('state1')
		if Request[0:6] == 'state2':
			print('state2')
		if Request[0:6] == 'state3':
			print('state3')
		if Request[0:6] == 'state4':
			print('state4')
		return

	

server_address_httpd = ('192.168.66.19', 8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('start')
httpd.serve_forever()
from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import os
import schedule
import time

def job():
    print('Hello, World!')

class RequestHandler_httpd(BaseHTTPRequestHandler):
	def do_GET(self):
		global Request, test, data, case
		messagetosend = bytes('test', "utf")
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
		self.send_header('Content-Length', len(messagetosend))
		self.end_headers()
		self.wfile.write(messagetosend)
		Request = self.requestline
		Request = Request[5: int(len(Request)-9)]

		if Request[0:2] == 's1':
			data = Request[2:]
			case = 1
			print(Request[0:2])
			print(Request[2:])
		if Request[0:2] == 's2':
			print(Request[0:2])
			print(Request[2:])
			data = Request[2:]
			case = 2
		if Request[0:6] == 'state1':
			print(Request[0:6])
			data = 0
			case = 3
		if Request[0:6] == 'state2':
			print(Request[0:6])
			data = 0
			case = 4
		if Request[0:6] == 'state3':
			print(Request[0:6])
			data = 0
			case = 5
		if Request[0:6] == 'state4':
			print(Request[0:6])
			data = 0
			case = 6
		if Request[0:6] == 'state5':
			print(Request[0:6])
			data = 0
		return

if __name__ == '__main__':
	server_address_httpd = ('192.168.66.19', 8080)
	httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
	print('start')
    schedule.every().seconds.do(job)
	httpd.serve_forever()

while True:
    schedule.run_pending()
    time.sleep(1)
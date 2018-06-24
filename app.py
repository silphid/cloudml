#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		self.wfile.write(bytes('test!', 'utf-8'))

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port' , PORT_NUMBER)
	server.serve_forever()

except KeyboardInterrupt:
	server.socket.close()
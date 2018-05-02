#!/usr/bin/env python3
# coding=utf-8

import http.server
import os
import cgi

HOST = "0.0.0.0"
PORT = 9000

class CustomServer(http.server.BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.sendHeader()

	def do_GET(self):
		contentType = "text/html"
		fileName = "." + self.path
		dummy, extension = os.path.splitext(self.path)

		if extension == ".css":
			contentType = "text/css"
		elif self.path == "/":
			fileName = "./index.html"

		self.sendHeader(contentType)
		try:
			text = open(fileName, "rb")
			self.wfile.write(text.read())
		except:
			self.sendFailHeader()

	def do_POST(self):
		f = cgi.FieldStorage(
			fp = self.rfile,
			headers = self.headers,
			environ = {
				'REQUEST_METHOD' : 'POST',
				'CONTENT_TYPE' : self.headers['Content-Type'],
			})

		for key in f.keys():
			data = f[key].file.read()
			with open("uploaded/" + f[key].filename, 'wb') as outf:
				outf.write(data)

	def sendHeader(self, content_type):
		self.send_response(200)
		self.send_header("Content-type", content_type)
		self.end_headers()

	def sendFailHeader(self):
		self.send_response(404)
		self.end_headers()

if __name__ == "__main__":
	server = http.server.HTTPServer((HOST, PORT), CustomServer)
	try:
		if not os.path.exists("uploaded"):
			os.makedirs("uploaded")
		print("hello!")
		server.serve_forever()
	except KeyboardInterrupt:
		print("goodbye!")
		server.shutdown()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urlparse

class HTTP(BaseHTTPRequestHandler):

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	
	def _headers_redirect(self, url):
		self.send_response(302)
		self.send_header('Location', 'http://atacante.com/?id=login&next=' + url)
		self.end_headers()
		
	def _get_query_id(self, path):
		url = urlparse.urlparse(path)
		try:
			return urlparse.parse_qs(url.query)['page'][0]
		except:
			return "login"

	def do_GET(self):
		id_url = self._get_query_id(self.path)
		
		if id_url=="login":
			self._set_headers()
			self.wfile.write("<!doctype html><html><head> <meta charset='utf-8'></head><body><center><h1>¡Página de login!</h1></center></body></html>")
		else:
			self._headers_redirect(id_url)
			
		

def run(server_class=HTTPServer, handler_class=HTTP, port=80):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'Starting httpd...'
	httpd.serve_forever()

run()

from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

server_address = ('', 8001)  # Change this to the desired port number
httpd = HTTPServer(server_address, MyRequestHandler)

print(f'Server running at http://localhost:{server_address[1]}/')
httpd.serve_forever()

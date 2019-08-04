import http.server

PORT = 8003

class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi']

with http.server.HTTPServer(('127.0.0.1', PORT), Handler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()
import http.server

httpd = http.server.HTTPServer(("",8080), http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()
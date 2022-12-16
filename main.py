import socketserver
import http.server
PORT=8000
Handsy=http.server.SimpleHTTPRequestHandler
httpd=socketserver.TCPServer(("",PORT),Handsy)
httpd.serve_forever()
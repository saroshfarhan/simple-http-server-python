import SimpleHTTPServer
import SocketServer
port = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",port),Handler)
print "Serving at port", port
httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import time

hostName = ""
hostPort = 2050


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("<p>You accessed path: %s</p>" %
        self.path, "utf-8")) #	POST is for submitting data.
        print("Yay")

    def do_POST(self):
        print("incoming http: ", self.path)
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data)
        self.send_response(200)

        #client.close()

        #import pdb; pdb.set_trace()

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()

print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

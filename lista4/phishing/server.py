from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import ssl
from io import BytesIO


class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            f = open("index.html", "rb")
            self.wfile.write(f.read())
        else:
            self.send_error(404)

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print(self.data_string)
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Ops! Something went wrong 404.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

try:
    httpd = HTTPServer(('localhost', 4443), MyHttpRequestHandler)
    print("Created our server...")
    sslctx = ssl.SSLContext()
    sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
    sslctx.load_cert_chain(certfile='./certA.crt', keyfile="./privkeyA.pem")
    httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
    print("Our server is safe.")
    print("Serving...")
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.socket.close() 
    print("Socket closed.")
except socket.error as j:
    print(j, '<---------')

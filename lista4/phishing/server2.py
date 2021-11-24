from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl


httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
sslctx = ssl.SSLContext()
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='./certA.crt', keyfile="./privkeyA.pem")
httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
# For python3

# generate server.pem with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# how to run:
#    python py3.https.server.py
# in browser:
#    https://localhost

import http.server as hs
import ssl

httpd = hs.HTTPServer(('localhost', 443), hs.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
try:
  httpd.serve_forever()
except KeyboardInterrupt:
  logger.info("Server stopped by user")

import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import base64
import sys

class AuthHandler(SimpleHTTPRequestHandler):

    def do_AUTHHEAD(self):
        print "send header"
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global key
        ''' Present frontpage with user authentication. '''
        self.do_AUTHHEAD()
        captured_credentials  = self.headers.getheader('Authorization')
        print "Captured credentials:{}".format(base64.b64decode(captured_credentials.replace("Basic ","")))

def capture(HandlerClass = AuthHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    if len(sys.argv)<1:
        print "usage SimpleAuthServer.py [port]"
        sys.exit()
    capture()

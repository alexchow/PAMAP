import BaseHTTPServer
import SocketServer
from urlparse import urlparse, parse_qs

class PampRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def main_response(self):
        response = "hello. I am PAMP"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response)
        return

    def get_path_and_query(self):
        path = urlparse(self.path).path
        query = urlparse(self.path).query

    def do_GET(self):
        if self.path == '/':
            self.main_response();
        else:
            self.get_path_and_query()
            

def keep_running():
    return True;

def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                   handler_class=BaseHTTPServer.BaseHTTPRequestHandler):

    """
    This assumes that keep_running() is a function of no arguments which
    is tested initially and after each request.  If its return value
    is true, the server continues.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    while keep_running():
        httpd.handle_request()

if __name__ == "__main__":
    run_while_true(handler_class=PampRequestHandler)

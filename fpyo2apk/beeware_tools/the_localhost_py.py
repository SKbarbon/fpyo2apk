The_localhost_py_script = """
import threading
import subprocess

class LocalHoat :
    def __init__(self) -> None:
        import socketserver

        self.started = False
        with socketserver.TCPServer(("localhost", 0), None) as s:
            free_port = s.server_address[1]
            self.PORT = int(free_port)
    
    def start (self):
        threading.Thread(target=self.run_server, daemon=True).start()
    
    def run_server (self):
        import http.server
        import socketserver
        import threading
        import webbrowser
        import time
        import random
            
        PORT = self.PORT # Change this to the desired port number
            
        class MyHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass
            
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            self.started = True
            httpd.serve_forever()
"""
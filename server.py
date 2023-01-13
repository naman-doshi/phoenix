import os
import threading
import webbrowser
import time
import multiprocessing
from http.server import HTTPServer, SimpleHTTPRequestHandler


port = 49374
#int(49374)=hex(C0DE)
path = r"/Users/namandoshi/Desktop/mynsb"



def start_server(path, port = 8000, automaticallyOpen = True):
    os.chdir(path)
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    server.serve_forever()



start_server(path, port, False)
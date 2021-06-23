#!/usr/local/bin/python
import socket
from _thread import start_new_thread


def threaded(c):
    while True:
        data = c.recv(1024)
        if not data or data.decode() == 'close':
            break
        c.send(data)
    c.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    sock, addr = s.accept()
    start_new_thread(threaded, (sock,))

# второй вариант
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)


def server(conn, addr):
    while True:
        data = conn.recv(1024)
        if data == 'close' or not data: break
        conn.send(data)
    conn.close()


while True:
    conn, addr = s.accept()
    t = threading.Thread(target=server, args=(conn, addr))
    t.start()

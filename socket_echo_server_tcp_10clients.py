import socket
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data or data == 'close':
        conn.close()
        break
    conn.send(data)
    conn.close()
s.close()
"""
# второй вариант
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 2222))
    s.listen(10)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data.decode() == 'close': break
        conn.send(data)

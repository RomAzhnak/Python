import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Message: ")
msg = msg.encode(encoding="utf-8")
# msg = bytearray(msg, 'UTF-8')
sock.sendto(msg, ('127.0.0.1', 8888))

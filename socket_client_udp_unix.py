import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
msg = input("Message: ")
msg = msg.encode(encoding="utf-8")
# msg = bytearray(msg, 'UTF-8')
sock.sendto(msg, 'unix.sock')

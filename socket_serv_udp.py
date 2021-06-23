import socket
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))
while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message:', result.decode('UTF-8'))
"""
# второй вариант с WITH
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print('888 is bind')
    sock.bind(('127.0.0.1', 8888))
    while True:
        result = sock.recv(1024)
        print('Message:', result.decode('UTF-8'))

import socket


# IP and UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# При '0' резервируются все адреса данной сети
sock.bind(('127.0.0.1', 8888))

# Попытка принять 1024 байта
result = sock.recv(1024)

print('Message', result.decode('utf-8'))

sock.close()

import socket

HOST = '192.168.14.211'    # The remote host
PORT = 80              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(bytes('hello world', 'UTF-8'))
data = s.recv(1024)
s.close()
print('Received', repr(data))

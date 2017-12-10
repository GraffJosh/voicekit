import socket
import time

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_Port = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect((TCP_IP, TCP_Port))

client.send('test this port')
response = client.recv(4096)

print response

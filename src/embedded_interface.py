import socket
import time

TCP_IP = '192.168.1.113'
TCP_Port = 1234


# connect the client
# client.connect((target, port))

for i in range(10,100,10):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TCP_IP, TCP_Port))
    client.send('{set_servo:'+str(i)+'}')
    response = client.recv(4096)
    client.close()
    print response

import socket
import time
from thread import *

radiator_IP = '192.168.1.113'
radiator_port = 1234
HOST = '192.168.1.8'
PORT = 8080

# connect the client
# client.connect((target, port))
def main():
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        receive_socket.bind((HOST, PORT))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        syreceive_socket.exit()

    print 'Socket bind complete'

    receive_socket.listen(10)
    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = receive_socket.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        start_new_thread(clientthread ,(conn,))
    receive_socket.close()

#Function for handling connectionreceive_socket. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()


def set_servo(value):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((radiator_IP, radiator_port))
    client.send('{set_servo:'+str(value)+'}')
    response = client.recv(4096)
    client.close()
    return response

if __name__ == '__main__':
    main()

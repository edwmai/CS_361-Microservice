# Echo client program
import socket

HOST = '192.168.5.9'    # The remote host
PORT = 50007            # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        try:

            message = input('Random video game name (name/genre:{genre}/end):')
            if message == 'end':
                print('Goodbye')
                break
            else:
                s.sendall(message.encode('utf-8'))
            data = s.recv(1024)
            print('Received:', data.decode('utf-8'))
        except KeyboardInterrupt:
            print('Connection closed')
            break
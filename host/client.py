from socket import socket, AF_INET, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 65432

server.connect((HOST, PORT))

msg = 'Hello, world'
print(f'Sending: {msg}')

msg = msg.encode()
server.sendall(msg)

data = server.recv(1024)
data = data.decode()
print(f'Received: {data}')

server.close()
print('Connection closed')

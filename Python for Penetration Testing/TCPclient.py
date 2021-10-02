# Python 3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.18.4'
host = socket.gethostname()
port = 3000

client_socket.connect((host, port))

mensagem = client_socket.recv(1024) # Máximo de dados que podem ser rececbidos em bytes!

client_socket.close()

print(f'Mensagem : ' + mensagem.decode('ascii'))
# Python 3

import socket

server_socket = socket.socket(
    socket.AF_INET, # IPV4
    socket.SOCK_STREAM # Tipo de comunicação (Protocolo de Conexão TCP/IP)
) # Object w/ Type + Protocol

# host = '192.168.18.4'
host = socket.gethostname() # GET IPAddress
port = 3000

server_socket.bind((host, port))

server_socket.listen(3) # Máximo de conexão por momento é 3!

while True:
    # Starting Connection!
    client_socket, address = server_socket.accept()

    print(f'Endereço : {address}')

    mensagem = "Hello!"
    client_socket.send(mensagem.encode('ascii'))
    client_socket.close()
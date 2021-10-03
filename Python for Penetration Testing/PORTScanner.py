# Python 3

import socket

def portScanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 (AF_INET) / TCP = (SOCK_STREAM)
    s.settimeout(15)

    if s.connect_ex((ip, port)): # IF Exception
        print("PORT CLOSED!")
    else:
        print("PORT OPEN !")


ip = input("IP : ")
port = int(input("PORT : "))
portScanner(ip, port)
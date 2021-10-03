# Python 3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    print( str(s.recv(1024)).strip('b') )

def main():
    ip = input("IP : ")
    port = int(input("PORT : "))
    banner(ip, port)

main()
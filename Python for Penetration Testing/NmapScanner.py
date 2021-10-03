# Python 3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool!")
print("<--------------------------------------------->")

ip_addr = input("IP : ")

print("\n")
print("1 | SYN ACK Scan")
print("2 | UDP Scan")
print("3 | Comprehensive Scan")
print("\n")

answer = input("Code : ")
print("\n")

print(f'Nmap Version : {scanner.nmap_version()}')

if answer == '1':
    
    scanner.scan(ip_addr, '1-1024', '-v -sS') # 1-1024 é o número de portas a serem escaneadas!
    print(f'IP Status : {scanner[ip_addr].state()}')
    print(f'Scan Info : {scanner.scaninfo()}')
    print(f'Protocols : {scanner[ip_addr].all_protocols()} ')

    if scanner[ip_addr].state() != 'down':
        print(f"Open Ports: {scanner[ip_addr]['tcp'].keys()} ")

elif answer == '2':

    scanner.scan(ip_addr, '1-1024', '-v -sU') # 1-1024 é o número de portas a serem escaneadas!
    print(f'IP Status : {scanner[ip_addr].state()}')
    print(f'Scan Info : {scanner.scaninfo()}')
    print(f'Protocols : {scanner[ip_addr].all_protocols()} ')

    if scanner[ip_addr].state() != 'down':
        print(f"Open Ports: {scanner[ip_addr]['udp'].keys()} ")

elif answer == '3':

    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O') # 1-1024 é o número de portas a serem escaneadas!
    print(f'IP Status : {scanner[ip_addr].state()}')
    print(f'Scan Info : {scanner.scaninfo()}')
    print(f'Protocols : {scanner[ip_addr].all_protocols()} ')

    if scanner[ip_addr].state() != 'down':
        print(f"Open Ports: {scanner[ip_addr]['tcp'].keys()} ")

else:
    
    print("Code not found!")
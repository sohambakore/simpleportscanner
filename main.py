print ('Simple Port Scanner**work in progress**')

import socket
ip = raw_input("Enter IP address: ")
port input("Enter Port: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sock_connect_ex((ip,port)):
    print ("Port",port,"Closed")
else:
    print ("Port",port,"Open")

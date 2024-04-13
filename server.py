from message import encapsulate, decapsulate
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)

socket.bind(('', 12000))

print('The server is ready to receive messages')
print('---------------------------------------')
while True:
    data, addr = socket.recvfrom(2048)
    seq, mesg = decapsulate(data.decode())

    print(f'{addr[0]}:{addr[1]}')
    print(seq, mesg)

    socket.sendto(encapsulate(seq, mesg).encode(), addr)
    print('---------------------------------------')

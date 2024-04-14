from packet import Packet
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)

socket.bind(('', 12000))

print('The server is ready to receive messages')
print('---------------------------------------')
while True:
    data, addr = socket.recvfrom(2048)

    packet = Packet()
    packet.decapsulate(data.decode())

    print(f'{addr[0]}:{addr[1]}')
    print(packet.seq, packet.mesg)

    socket.sendto(packet.encapsulate().encode(), addr)
    print('---------------------------------------')

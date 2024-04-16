from packet import Packet
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)

socket.bind(('', 12000))

current = 0

print('The server is ready to receive messages')
print('---------------------------------------')
while True:
    data, addr = socket.recvfrom(2048)

    packet = Packet()
    packet.decapsulate(data.decode())

    print(f'{addr[0]}:{addr[1]}')
    print(packet.seq, packet.end, packet.flag, packet.mesg)

    if (packet.seq == current):
        current += 1
    else:
        packet.seq = current
        packet.flag = 1

    socket.sendto(packet.encapsulate().encode(), addr)
    print('---------------------------------------')

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

    if (packet.seq == current):
        print(f'{addr[0]}:{addr[1]}')
        print(packet.seq, packet.end, packet.flag, packet.mesg)
        print('---------------------------------------')
        current += 1
    elif (packet.seq < current):
        continue
    else:
        packet.seq = current
        packet.flag = 1

    socket.sendto(packet.encapsulate().encode(), addr)

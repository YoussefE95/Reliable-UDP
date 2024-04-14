from packet import Packet
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)
window = 10
timeout = 60

def batch(seq_range, mesg):
    packets = []

    for seq in seq_range:
        packets.append(Packet(seq, 0, mesg))

    return packets

def send(packets, addr, port):
    for packet in packets:
        socket.sendto(packet.encapsulate().encode(), (addr, port))

def recv(packets):
    start = time.perf_counter()

    while(len(packets) > 0 and time.perf_counter() - start < timeout):
        data, addr = socket.recvfrom(2048)
        packet = Packet(data.decode())

        if (packet == packets[0]):
            packets.remove(packet)
            print(packet)
        elif (packet in packets[1:]):
            index = packets.index(packet)
            packets = packets[index:]
            print(packets[0:index])

def main():
    dest = input('Destination: ')
    mesg = input('Message: ')
    total = int(input('Number times to send: '))

    addr = dest.split(':')[0]
    port = int(dest.split(':')[1])

    print('\n-------------------------------------------')
    for i in range(0, total, window):
        batch_len = i + window

        if (batch_len > total):
            batch_len = total

        packets = batch(range(i, batch_len), mesg)

        while(len(packets) > 0):
            send(packets, addr, port)
            recv(packets)
        print('-------------------------------------------')

    socket.close()

if __name__ == '__main__':
    main()

from packet import Packet
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)
window = 10
timeout = 60

socket.settimeout(5)

def batch(start, end, mesg):
    packets = []

    for seq in range(start, end):
        packets.append(Packet(seq, end, 0, mesg))

    return packets

def send(packets, addr, port):
    for packet in packets:
        socket.sendto(packet.encapsulate().encode(), (addr, port))

def recv(packets):
    try:
        while(len(packets) > 0):
            seq_nums = [packet.seq for packet in packets]
            packet = Packet()

            data, addr = socket.recvfrom(2048)
            packet.decapsulate(data.decode())

            print(packet.seq, packet.end, packet.flag, packet.mesg)

            if (packet.flag == 1):
                packets = batch(packet.seq, packet.end, packet.mesg)
            elif (packet.seq in seq_nums):
                for j in range(0, seq_nums.index(packet.seq) + 1):
                    packets.pop(0)
    except:
        print('Timeout')

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

        packets = batch(i, batch_len, mesg)

        while(len(packets) > 0):
            send(packets, addr, port)
            recv(packets)
        print('-------------------------------------------')

    socket.close()

if __name__ == '__main__':
    main()

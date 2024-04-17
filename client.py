from packet import Packet
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)
socket.settimeout(5)
window = 10

# Returns an array of Packet with sequence
# numbers in range(start, end)
def batch(start, end, mesg):
    packets = []

    print(f'Building batch in range {start}-{end}')

    for seq in range(start, end):
        packets.append(Packet(seq, end, 0, mesg))

    return packets

# Sends all packets to the given destination
def send(packets, addr, port):
    for packet in packets:
        socket.sendto(packet.encapsulate().encode(), (addr, port))

# Handles any incoming responses from the server
def recv(packets):
    try:
        while(len(packets) > 0):
            # Get all un-ACK'd seq nums in current window
            seq_nums = [packet.seq for packet in packets]
            packet = Packet()

            # Read in data and decapsulate into Packet object
            data, addr = socket.recvfrom(2048)
            packet.decapsulate(data.decode())

            print(packet.seq, packet.end, packet.flag, packet.mesg)

            # Flag equalling 1 means server sent NAK
            if (packet.flag == 1):
                # Check if we've recieved this NAK before
                if (packet.seq != seq_nums[0]):
                    # Update the packets batch to resend request packet
                    # and following packets in the current window
                    packets = batch(packet.seq, packet.end, packet.mesg)
            elif (packet.seq in seq_nums):
                # We can handle cumulative ACK by assuming packet seq N
                # would not have been ACK'd without N-1 being recieved.
                # Therefore, we can clear the current seq being ACK'd
                # and all seq nums less than it too
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

    # Loop over windw length
    print('\n-------------------------------------------')
    for i in range(0, total, window):
        batch_len = i + window

        # For the last batch which may be less than the
        # window size
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

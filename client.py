from message import encapsulate, decapsulate
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)
window = 10
timeout = 60

def send(mesg, addr, port, seqRange):
    for seq in seqRange:
        socket.sendto(encapsulate(seq, mesg).encode(), (addr, port))

def recv(batch):
    start = time.perf_counter()
    while(len(batch) > 0 and time.perf_counter() - start < timeout):
        resp, respAddr = socket.recvfrom(2048)
        ack, respMsg = decapsulate(resp.decode())
 
        if (ack in batch):
            batch.remove(ack)
            print(ack, respMsg)

dest = input('Destination: ')
mesg = input('Message: ')
total = int(input('Number times to send: '))

addr = dest.split(':')[0]
port = int(dest.split(':')[1])

print('\n-------------------------------------------')
for i in range(0, total, window):
    batchLength = i + window

    if (batchLength > total):
        batchLength = total
    
    seqRange = range(i, batchLength)
    batch = list(seqRange)

    send(mesg, addr, port, seqRange)
    
    while(len(batch) > 0):
        recv(batch)

    print('-------------------------------------------')

socket.close()

headerSize = 8

def encapsulate(seq, msg):
    pad = ' ' * (headerSize - len(str(seq)))
    return f'{pad}{seq}{msg}'

def decapsulate(data):
    return int(data[0:8]), data[8:]

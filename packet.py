seq_len = 8
flag_len = 1

class Packet:
    def __init__(self, seq=0, flag=0, mesg=''):
        self.seq = seq
        self.flag = flag
        self.mesg = mesg

    def seq_header(self):
        pad = ' ' * (seq_len - len(str(self.seq)))
        return f'{pad}{self.seq}'

    def flag_header(self):
        pad = ' ' * (flag_len - len(str(self.flag)))
        return f'{pad}{self.flag}'

    def encapsulate(self):
        return f'{self.seq_header()}{self.flag_header()}{self.mesg}'

    def decapsulate(self, data):
        self.seq = data[0:seq_len]
        self.flag = data[seq_len:flag_len]
        self.mesg = data[flag_len:]


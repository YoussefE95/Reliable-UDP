seq_len = 8
flag_len = 1

class Packet:
    def __init__(self, seq = 0, end = 0, flag = 0, mesg = ''):
        self.seq = seq
        self.end = end
        self.flag = flag
        self.mesg = mesg

    def seq_header(self):
        pad = ' ' * (seq_len - len(str(self.seq)))
        return f'{pad}{self.seq}'

    def end_header(self):
        pad = ' ' * (seq_len - len(str(self.end)))
        return f'{pad}{self.end}'

    def flag_header(self):
        pad = ' ' * (flag_len - len(str(self.flag)))
        return f'{pad}{self.flag}'

    def encapsulate(self):
        headers = f'{self.seq_header()}{self.end_header()}{self.flag_header()}'
        return f'{headers}{self.mesg}'

    def decapsulate(self, data):
        seq_index = seq_len
        end_index = 2 * seq_len
        flag_index = end_index + flag_len

        self.seq = int(data[0:seq_index])
        self.end = int(data[seq_index:end_index])
        self.flag = int(data[end_index:flag_index])
        self.mesg = data[flag_index:]


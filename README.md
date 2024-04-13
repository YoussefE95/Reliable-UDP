
# How to use
Run server.py
```python server.py```

Run client.py 
```python client.py```

You will be prompted the following (on Client.py):
```
Destination: 
Message:
Number times to send: 
```
Destination example: `localhost:12000` or `127.0.0.1:12000`
Message example: `Hello!`
Number times example: `10`

Note: hit `Enter` after each input

Here is an example of how it can look

```
Destination: localhost:12000
Message: Howdy
Number times to send: 10
```

# Purpose of this code

The purpose of this code is to build on top of UDP by adding extra headers to create more reliability of ensuring messages are being sent.

# Architecture/Design
client.py
```
def send(mesg, addr, port, seqRange):

def recv(batch):

def main():

```

message.py
```
def encapsulate(seq, msg):
    """
    Sum up the different parts of the payload including sequence number and the message into a single string. This method also has a max header size of 8. 
    
    Returns:
        string: formated by any necessary padding, sequence number, and the message
    Example:
        >>> seq, msg = 100, 'Howdy'
        >>> packet = encapsulate(seq, msg)
        >>> packet
        '   100Howdy' 
        #Note the padding
    """

def decapsulate(data):
    """
    Split up the data/packet into its respective components: headers (first 8 characters) and message (anything after 8 characters). Note: converting string to integers will remove any padding spaces used.
    
    Returns:
        integer, string: the first 8 characters are converted into integers and the anything after the 8th character is the message
    Example:
        >>> data = '   100Howdy'
        >>> packet = decapsulate(data)
        >>> packet
        100, 'Howdy' 
    """
```

server.py
```

def main():
```

# Error Detection
Packets are being sent as strings, but to increment SEQ# or ACK then we will need to convert to integer type.

### Output

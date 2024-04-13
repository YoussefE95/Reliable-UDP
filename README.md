
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
Destination example: `x.x.x.x:12000`
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
The purpose of this code is to build on top of UDP by adding extra headers to create more reliability
of ensuring messages are being sent.

# Architecture/Design
client.py
```
def send(mesg, addr, port, seqRange):
  """
  Sends x messages to server where x is the window size. The server is connected with a socket with addr and port
  
  Returns:
    None
  Example:
    >>> mesg, addr, port, seqRange = 'Howdy', localhost, 12000, 10
    >>> send(mesg, addr, port, seqRange)
  """

def recv(batch):
  we print only if ack
  """
  receives x messages from server while batch is not empty. If the message hasn't timed out, wait for the acknowledgement for each message. If we receive the acknowledgement, we remove the corresponding sequence number from the batch list and prints the acknowledgement + message received from the server.
  
  Returns:
    None
  Example:
    >>> seqRange = range(i, batchLength) # (0, 10)
    >>> batch = list(seqRange)           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> recv(batch)                      # wait, receive, and check 0-9 acknowledgements
  """

def main():
  """
  initiate and ask the user for destination addr:port, contents of message, and total number of N times to send the message. 
  
  Iterate through total N messages by steps of size window/"batch" size (e.g. 10). Most batches are the same size, and we accounted for the case where the last batch is less than the window size (e.g 3 messages remaining when window/batch size was 10). As we iterate, we send batches of messages and then wait to receive their acknowledgements

  Returns:
    None
   """
```

message.py
```
def encapsulate(seq, msg):
  """
  Sum up the different parts of the payload including sequence number and the message 
  into a single string. This method also has a max header size of 8. 
  
  Returns:
    string: formated by any necessary padding, sequence number, and the message
  Example:
    >>> seq, msg = 0, 'Howdy'
    >>> packet = encapsulate(seq, msg)
    >>> packet
    b'    0howdy' 
    #Note the padding
  """

def decapsulate(data):
  """
  Split up the data/packet into its respective components: headers (first 8 characters) and message (anything after 8 characters). Note: converting string to integers will remove any padding spaces used.
  
  Returns:
    integer, string: the first 8 characters are converted into integers and the anything after the 8th character is the message
  Example:
    >>> data = '  100Howdy'
    >>> packet = decapsulate(data)
    >>> packet
    100, 'Howdy' 
  """
```

server.py
```

def main():
```

# Install NetEM
```
sudo apt-get ...
```

# Tests and their Output
## Condition 1 (No latency or loss): Send 100 messages from client to server. 
```python client.py```
```
Destination: x.x.x.x:12000
Message: Howdy
Number times to send: 100
```
### client and server output:
<insert image here>

## Condition 2.1 (Artificial Latency, No Loss) 
- Add enough delay time using NetEm to trigger your timeout timer and generate conditions for retransmission. 

### client and server output:
Note: output should show timeout and retransmissions
<insert image here>

## Condition 2.2 (No Latency, Artificial Loss) 
- Add 10% packet loss using NetEm to trigger retransmissions. 

```
```

### client and server output:
Note: output should show retransmissions timeout and retransmissions
<insert image here>


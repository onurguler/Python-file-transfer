import socket


HOST = socket.gethostbyname("192.168.0.104")        # Write your IP Adress Here
PORT = 8080
s = socket.socket()

s.connect((HOST, PORT))
s.send(b'Hello server!')

with open('received_file', 'wb') as f:
    print('File opened')
    while True:
        print('Receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('Succesfully get the file')
s.close()
print('Connection closed')

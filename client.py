import socket


HOST = socket.gethostbyname("192.168.0.104")
PORT = 60000
s = socket.socket()

s.connect((HOST, PORT))
s.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print("file opened")
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        f.write(data)

f.close()
print('Succesfully get the file')
s.close()
print('connection closed')

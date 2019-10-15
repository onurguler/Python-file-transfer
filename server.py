import socket

PORT = 8080
s = socket.socket()
HOST = socket.gethostname()
s.bind((HOST, PORT))
s.listen(5)


print("Server Listening........")

while True:
    conn, addr = s.accept()
    print("Got connection from", addr)
    data = conn.recv(1024)
    print("Server received", repr(data))

    filename = "myText.txt"
    f = open(filename, "rb")
    l = f.read(1024)
    while (l):
        conn.send(l)
        print("Send ", repr(l))
        l = f.read(1024)
    f.close()

    print("Done Sending")
    conn.send(b"Thank you for connecting")
    conn.close()

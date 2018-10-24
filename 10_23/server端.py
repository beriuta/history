import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
while True:
    conn,addr = sk.accept()
    data = conn.recv(8090)
    print(data)
    conn.send(b'ok')
    conn.close()
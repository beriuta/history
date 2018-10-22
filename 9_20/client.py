from socket import *
client = socket(AF_INET,SOCK_STREAM)
client.connect(('192.168.16.108',9001))
while True:
    msg = input('>>>')
    if not msg:continue
    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode('utf-8'))
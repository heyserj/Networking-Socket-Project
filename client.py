import socket
import sys
import re

fullUrl = sys.argv[1]
url = re.findall('(\w.+):', fullUrl)
url = url[0]

port = re.findall(':(\w+)/', fullUrl)
port = int (port[0])

filePath = re.findall('/(\w./+)', fullUrl)

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((url, port))

msg = 'GET ' + filePath[0] + ' HTTP/1.1\r\n\r\n'

mySocket.send(msg.encode())
while True:
    data = mySocket.recv(1024)

    if len(data) < 1:
        break
    print(data.decode())

mySocket.close()

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
portno = 6789
serverSocket.bind(('', portno))
serverSocket.listen(1)
while True:
#Establish the connection
print ('Ready to serve...')
connectionSocket, addr = serverSocket.accept()
try:
 message = connectionSocket.recv(1024)
 filename = message.split()[1]
 f = open(filename[1:])
 outputdata = f.read()
#Send one HTTP header line into socket
 connectionSocket.send(bytes('HTTP/1.1 200 OK \r\n\r\n','UTF-8'))
#Send the content of the requested file to the client
 for i in range(0, len(outputdata)):
 connectionSocket.send(bytes(outputdata[i], 'UTF-8'))
 connectionSocket.close()
except IOError:
#Send response message for file not found
 connectionSocket.send(bytes('HTTP/1.1 404 Not Found \r\n\r\n 404 Not Found', 'UTF-8'))
#Close client socket
connectionSocket.close()
serverSocket.close()
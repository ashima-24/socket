from socket import*
serverName='mpi-inf.mpg.de'
serverPort=666
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=raw_input('Hello')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print modifiedMessage.decode()
clientSocket.close()


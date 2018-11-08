import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='snoopy.mpi-inf.mpg.de'
port=666
s.connect((host,port))
s.send("HELLO.\n")
msg=s.recv(1024)
print msg.decode('ascii')
s.send(".\n")
s.close()



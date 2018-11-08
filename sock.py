import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='snoopy.mpi-inf.mpg.de'
port=666
s.connect((host,port))
msg=s.recv(1024)
s.close()
print(msg.decode('ascii'))


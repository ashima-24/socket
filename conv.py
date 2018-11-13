import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='snoopy.mpi-inf.mpg.de'
port=666
pos=0
s.connect((host,port))
s.send(b"HELLO.\n")
s.send(b"DOWNLOAD.\n:")
data=b""
with open ('conv.txt','wb') as f:
    while 1:
        msg=s.recv(1024)
        if not msg:
                   break
        else:
             data+=msg
             #print(msg)
#             f.write(msg)
file=open("conv.txt",'rb+')
file.seek(56)
file.write(b"62531")
s.close()

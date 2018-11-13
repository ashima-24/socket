import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='snoopy.mpi-inf.mpg.de'
port=666
pos=0
s.connect((host,port))
s.send(b"HELLO.\n")
s.send(b"DOWNLOAD.\n:")
data=b""
m=0
with open ('abc.txt','wb') as f:
    while 1:
        msg=s.recv(1024)
        if not msg:
            break
        else:
             print(msg)
             data+=msg
             pos=pos+1
        if pos>=5:
                 print(msg)
                 m=data.find(b"TOKEN")
                 if m==62587:
                             break
                 f.write(msg)
s.close()



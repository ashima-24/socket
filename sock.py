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
while 1:
        msg=s.recv(1024)
        if not msg:
            break
        else:
             data+=msg

b=data.split(b'\n')[3]
img=b.split()[1]
print(img)
H=data.split(b'BYTES')
t=H[1].split(b'TOKEN')
#print(t[0])
img1=bytearray(t[0]).lstrip(b'\n')
print(len(img1))
with open('img.jpeg','wb') as ima:
  ima.write(img1)
s.close()



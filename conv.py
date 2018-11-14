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
            f.write(msg)


#print(data.split(b'\n')[0])
#print(data.split(b'\n')[1])
#print(data.split(b'\n')[2])
b=data.split(b'\n')[3]
img=b.split()[1]
print(img)



#print(img1[1])
#print(data.split(b'TOKEN')[1])
H=data.split(b'BYTES')
t=H[1].split(b'TOKEN')
#print(t[0])
img1=bytearray(t[0])
img3=img1.lstrip(b'\n')
print(img3)
with open ('cat.jpeg','wb') as i:
   i.write(img3)
tok=t[1].split(b'\n')
token=tok[0].split(b':')
#print(token[1])
with open ('token.txt','wb') as w:
    w.write(token[1])
s.close()

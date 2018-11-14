import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'snoopy.mpi-inf.mpg.de'
PORT = 666

s.connect((HOST, PORT))

s.send(b"HELLO.\n")
s.send(b"DOWNLOAD.\n:")

DATA = b""
SIZE = 1024
CAT = 'CAT.jpeg'
TO = 'TOKEN.txt'

while True:
       msg = s.recv(SIZE)
       if not msg:
                 break
       else:
            DATA += msg

start = DATA.split(b'\n')
helo = DATA.split(b'\n')[0]
comand = DATA.split(b'\n')[1]
fil = DATA.split(b'\n')[2]
b = DATA.split(b'\n')[3]
img = b.split()[1] # no of bytes of images

H = DATA.split(b'BYTES')
t = H[1].split(b'TOKEN')

img3 = t[0].lstrip(b'\n')  # raw bytes of image

with open(CAT, 'wb') as i:
    i.write(img3)   # writing image in CAT.jpeg

tok = t[1].split(b'\n')
token = tok[0].split(b':')
token = token[1].split()  # 32 bit token

with open(TO, 'wb') as w:
    w.write(token[0]) # writing token in TOKEN.txt

s.close()

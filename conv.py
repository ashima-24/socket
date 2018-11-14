import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'snoopy.mpi-inf.mpg.de'
PORT = 666

s.connect((HOST, PORT))

s.send(b"HELLO.\n")
s.send(b"DOWNLOAD.\n:")

data = b""
size=1024
cat='CAT.jpeg'
to='TOKEN.txt'

while 1:
       msg = s.recv(size)
       if not msg:
                 break
       else:
            data += msg

start = data.split(b'\n')
helo = data.split(b'\n')[0]
comand = data.split(b'\n')[1]
fil = data.split(b'\n')[2]
b = data.split(b'\n')[3]
img = b.split()[1] # no of bytes of images

H = data.split(b'BYTES')
t = H[1].split(b'TOKEN')

img1 = bytearray(t[0])
img3 = img1.lstrip(b'\n')  # raw bytes of image


with open(cat, 'wb') as i:
    i.write(img3)   # writing image in CAT.jpeg


tok = t[1].split(b'\n')
token = tok[0].split(b':')
token=token[1].split()  # 32 bit token

with open(to, 'wb') as w:
    w.write(token[0]) # writing token in TOKEN.txt

s.close()

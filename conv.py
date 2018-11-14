import socket
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'snoopy.mpi-inf.mpg.de'
PORT = 666
S.connect((HOST, PORT))
S.send(b"HELLO.\n")
S.send(b"DOWNLOAD.\n:")
DATA = b""
while 1:
       MSG = S.recv(1024)
       if not MSG:
                 break
       else:
           DATA += MSG

START = DATA.split(b'\n')
HELO = DATA.split(b'\n')[0]
print(HELO)
COMAND = DATA.split(b'\n')[1]
print(COMAND)
FIL = DATA.split(b'\n')[2]
print(FIL)
B = DATA.split(b'\n')[3]
print(B)
IMG = B.split()[1]
print(IMG) # no of bytes of images

H = DATA.split(b'BYTES')
T = H[1].split(b'TOKEN')

IMG1 = bytearray(T[0])
IMG3 = IMG1.lstrip(b'\n')
print(IMG3)   # raw bytes of image

with open('CAT.jpeg', 'wb') as I:
    I.write(IMG3)

TOK = T[1].split(b'\n')
TOKEN = TOK[0].split(b':')
print(TOKEN[1])  # 32 bit token

with open('TOKEN.txt', 'wb') as W:
    W.write(TOKEN[1])

S.close()

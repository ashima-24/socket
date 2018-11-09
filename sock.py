import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='snoopy.mpi-inf.mpg.de'
port=666
i=0
s.connect((host,port))
s.send(b"HELLO.\n")
s.send(b"DOWNLOAD.\n")
while 1 :
            msg=s.recv(10)
            print(msg)      
            if msg=='b': 
             break
                   
s.close()



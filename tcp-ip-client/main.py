import socket


TCP_IP = input("Enter IP: ")
TCP_PORT = int(input("Enter Port: "))
BUFFER_SIZE = 1000000
MESSAGE = input("Input Team Name: ")
PASSWORD = input("Input Password: ")
SEND = MESSAGE + " " + PASSWORD + "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendto(SEND.encode(), (TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

path = "C:\\nbcc-hack-a-thon\\image.png"
newf = open(path,'wb')
newf.write(data)

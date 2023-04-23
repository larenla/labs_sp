import socket
import uuid
print("Vvedite imya")
i = input()
print("privet, ",i,"!!")

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("HOSTNAME",hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("IP ADDRESS",s.getsockname()[0])
s.close()
print("Your LOCAL IP Address : "+IPAddr)
print ("Your MAC address : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >  ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

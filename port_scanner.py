import sys
import socket
from datetime import datetime

#Define your target :: 
if len(sys.argv) == 2 :
    target = socket.gethostbyname(sys.argv[1]) #translate host name to ipv4
else :
    print("Invalid amount of arguments !!")
    print("Syntax : python3 port_scanner.py <ip> ")

#banner ::

print("-" * 50)
print("scanning target " + target)
print("time started " + str(datetime.now()))
print("-" *50)

try:
    for port in range (1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))#return error indicator
        if result== 0:
            print("port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("could not connect to server.")
    sys.exit()
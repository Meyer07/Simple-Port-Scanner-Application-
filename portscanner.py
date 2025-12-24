import time 
import socket

target="scanme.nmap.org"
print(f"Beginning scan on:{target}")


start_time=time.time()

##for loop to scan all possible ports on a network
for port in range(1,1024):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ##timeout ensures that the program doesn't crash 
    ##AF_INET and SOCK_STREAM are functions of the socket imports, check if the network is IVP4 and what kind of connection 
    ##the network runs on 
    s.settimeout(0.5)

    ##checks if a port is open and connected to properly 
    result =s.connect_ex((target,port))


    if result==0:
        print(f"Found Open Port:{port}")
    
    s.close()

print(f"Scan Complete in {time.time()-start_time:.2f}s")
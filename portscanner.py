import time 
import socket

target="scanme.nmap.org"

print(f"Beginning scan on:{target}")


start_time=time.time()

for port in range(1,1024):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)

    result =s.connect_ex((target,port))


    if result==0:
        print(f"Found Open Port:{port}")
    
    s.close()

print(f"Scan Complete in {time.time()-start_time:.2f}s")
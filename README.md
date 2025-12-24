# Simple-Port-Scanner-Application-
This is a lightweight port scanner that demonstrates my Cyber Security knowledge and network security.

NOTICE: any other developers looking at this repo, port scanning without express legal consent from the network owner is legally ambigugous to illegal, only scan legally in order to not face the rather of a coporate legal department


Featres:
*Fast TCP port scanning
*Configurable timeout settings
*Scan completion time reporting
*Easy-to-modify target and port range


Requirements:
*Python 3.x
*No External Dependencies


Running:
if implemented correctly the scanner should produce a terminal output in VS Code like this
Beginning scan on: 192.168.1.1
Found Open Port: 22
Found Open Port: 80
Found Open Port: 443
Scan Complete in 12.34s

Limitations:
*Only scans TCP ports not UDP
*sequential scanning(no multithreading implementation)
*Basic functionality without service detection


Author: Sam Meyer 

under the MIT Licesnes this repo is open source and can be edited via pull requests

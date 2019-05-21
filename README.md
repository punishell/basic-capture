# basic-capture
Simple server written in python 2.7 to capture credentials via HTTP Basic Authentication.

Inspirated taken from smb-capture module in Metasploit. 
Receommended to chain up with SSRF vulnerability to check if application will pass crendentials via HTTP Basic Auth.

#Usage 

root@trustmeimprinter:~# python basic-capture.py 
Serving HTTP on 0.0.0.0 port 8000 ...
send header
127.0.0.1 - - [21/May/2019 03:39:19] "GET / HTTP/1.1" 401 -
None
send header
127.0.0.1 - - [21/May/2019 03:39:24] "GET / HTTP/1.1" 401 -
Basic dGVzdDp0ZXN0


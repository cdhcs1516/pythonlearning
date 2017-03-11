# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 16:47:34 2017

@author: Administrator
"""

#!/user/bin/env python

from socket import *

Host = 'localhost'
Port = 21567
BufSZ = 1024
Addr = (Host, Port)

tcpClisock = socket(AF_INET, SOCK_STREAM)
tcpClisock.connect(Addr)

while True:
  data = raw_input('> ')
  if not data:
    break
  tcpClisock.send(data)
  data = tcpClisock.recv(BufSZ)
  if not data:
    break
  print data
  
tcpClisock.close()
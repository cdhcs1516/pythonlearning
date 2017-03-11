# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 16:46:19 2017

@author: Administrator
"""

#!/usr/bin/env python

from socket import *
from time import ctime

Host = ''
Port = 21567
BufSZ = 1024
Addr = (Host, Port)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(Addr)
tcpSerSock.listen(5)

try:
  while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr
    
    while True:
      data = tcpCliSock.recv(BufSZ)
      if not data:
        break
      tcpCliSock.send('[%s] %s' % (ctime(), data))
      
    tcpCliSock.close()
except Exception, ex:
  print 'Incorrect input', ex
  tcpSerSock.close()
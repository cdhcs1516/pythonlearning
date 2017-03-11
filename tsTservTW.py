# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 21:26:42 2017

@author: Administrator
"""

#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

Port = 31245

class TSServProtocol(protocol.Protocol):
  def connectionMade(self):
    clnt = self.clnt = self.transport.getPeer().host
    print '...connection from:', clnt
  def dataReceived(self, data):
    self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(Port, factory)
reactor.run()
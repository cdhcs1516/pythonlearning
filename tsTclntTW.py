# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 21:35:20 2017

@author: Administrator
"""

#!/usr/bin/env python

from twisted.internet import protocol, reactor

Host = 'localhost'
Port = 21568

class TSClntProtocol(protocol.Protocol):
  def sendData(self):
    data = raw_input('> ')
    if data:
      print '...sending %s...' % data
      self.transport.write(data)
    else:
      self.transport.loseConnection()
      
  def connectionMade(self):
    self.sendData()
    
  def dataReceived(self, data):
    print data
    self.sendData()
  
class TSClntFactory(protocol.ClientFactory):
  protocol = TSClntProtocol
  clientConnectionLost = clientConnectionFailed = \
    lambda self, connector, reason: reactor.stop()
  
reactor.connectTCP(Host, Port, TSClntFactory())
reactor.run()
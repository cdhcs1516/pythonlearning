# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 22:04:53 2017

@author: Administrator
"""

#!/usr/bin/env python

db = {}

def newusr():
  prompt = 'login desired: '
  while True:
    name = raw_input(prompt)
    if db.has_key(name):
      prompt = 'name taken, try another: '
      continue
    else:
      break
  pwd = raw_input('passwd: ')
  db[name] = pwd

def oldusr():
  name = raw_input('login: ')
  pwd = raw_input('passwd: ')
  passwd = db.get(name)
  if passwd == pwd:
    print 'Welcome back', name
  else:
    print 'Login incorrect'
    
def showmenu():
  prompt = """
  (N)ew User Login
  (E)xisting User Login
  (Q)uit
  Enter choice: """
  
  done = False
  
  while not done:
    
    chosen = False
    while not chosen:
      try:
        choice = raw_input(prompt).strip()[0].lower()
      except (EOFError, KeyboardInterrupt):
        choice = 'q'
      print '\nYou picked: [%s]' % choice
      if choice not in 'neq':
        print 'Invalid option, try again'
      else:
        chosen = True
        
    if choice == 'q':done = True
    if choice == 'n':newusr()
    if choice == 'e':oldusr()
    
if __name__ == '__main__':
  showmenu()
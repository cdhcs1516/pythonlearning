# -*- coding: utf-8 -*-
"""Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python

import nntplib
import socket

Host = 'web.aioe.org'
Grnm = 'comp.lang.python'
User = 'wesley'
Pass = "you'llNeverGuess"

def main():
  try:
    n = nntplib.NNTP(Host)
    #, user = User, password = Pass
  except socket.gaierror, e:
    print 'ERROR: cannot reach host "%s"' % Host
    print '  ("%s")' % eval(str(e))[1]
    return
  except nntplib.NNTPPermanentError, e:
    print 'ERROR: access denied on "%s"' % Host
    print '  ("%s")' % str(e)
    return
  print '*** Connected to host "%s"' % Host
  
  try:
    rsp, ct, fst, lst, grp = n.group(Grnm)
  except nntplib.NNTPTemporaryError, e:
    print 'ERROR: cannot load group "%s"' % Grnm
    print '  ("%s")' % str(e)
    print '  Server may require authentication'
    print '  Uncomment/edit login line above'
    n.quit()
    return
  except nntplib.NNTPPermanentError, e:
    print 'ERROR: group "%s" unavailable' % Grnm
    print '  ("%s")' % str(e)
    n.quit()
    return
  print '*** Found newsgroup "%s"' % Grnm
  
  rng = '%s-%s' % (lst, lst)
  rsp, frm = n.xhdr('from', rng)
  rsp, sub = n.xhdr('subject', rng)
  rsp, dat = n.xhdr('date', rng)
  print '''*** Found last article (#%s):
      
  From: %s
  Subject: %s
  Date: %s
'''% (lst, frm[0][1], sub[0][1], dat[0][1])
  
  rsp, anum, mid, data = n.body(lst)
  displayFirst20(data)
  n.quit()
  
def displayFirst20(data):
  print '*** First (<=20) meaningful lines:\n'
  count = 0
  lines = (line.rstrip() for line in data)
  lastBlank = True
  
  for line in lines:
    if line:
      lower = line.lower()
      if (lower.startswith('>') and not \
          lower.startswith('>>>')) or \
          lower.startswith('|') or \
          lower.startswith('in article') or \
          lower.endswith('writes: ') or \
          lower.endswith('wrote: '):
            continue
    if not lastBlank or (lastBlank and line):
      print '  %s' % line
      if line:
        count += 1
        lastBlank = False
      else:
        lastBlank = True
    if count == 20:
      break
    
if __name__ == '__main__':
  main()
  
  
    
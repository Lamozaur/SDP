#-*- coding: utf-8 -*-
print ord(u'ą')
print chr(99)
print ord('%')

errmsg = u"Nie można otworzyć pliku"
print errmsg
print errmsg + u', brak dostępu.'
print errmsg.split()
print u"Błąd: %s"%errmsg

file = 'myfile.txt'
print errmsg + ' ' + file

print "%s %s"%(errmsg, file)

print errmsg + u' ,brak dostępu.'

print errmsg.encode('iso-8859-2')
print errmsg.encode('utf-8')

msg = errmsg.encode('utf-8')
print msg.decode('utf-8')
print msg.decode('utf-8')
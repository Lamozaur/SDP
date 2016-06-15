#3.26-3.31
k = "uid"
v = "sa"
print "%s=%s" % (k,v)

uid = 'sa'
pwd = 'secret'
print pwd + " nie jest poprawnym haslem dla " + uid
"""userCount = 6
print " Uzytkownikow: %d % " + userCount"""

print "Dzisiejsza ceana aukcji: %f" % 50.4625
print "Dzisiejsza cena aukcji: %.2f" % 50.4625
print "Zmiana w stosunku do dania wczorajszego: %+.2f" % 1.5

li = [1,9,8,4]
print [element*2 for element in li]
print li
li = [elem*2 for elem in li]
print li

params =  {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
"""print params.keys()
print params.values()
print params.items()
print [k for k, v in params.items()]"""
print ["%s=%s"% (k,v) for k,v in params.items()]
print ";".join(["%s=%s" % (k, v) for k,v in params.items()])

li = ['pwd = secret', 'database = master','uid = sa', 'server = mpilgrim']
s = ";".join(li)
print s
print s.split(";")
print s.split(";",1)



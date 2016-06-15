import odbchelper
from apihelper import info
li=[]
"""print info(li)
print info(odbchelper)
print info(odbchelper, 30)
print info(odbchelper, 30, 0)"""

print info(odbchelper, collapse=0)
print info(spacing=15, object=odbchelper)

print type(1)
print type(li)
print type(odbchelper)

print str(1)
horsemen = ['war','pestilance', 'famine']
print horsemen
horsemen.append('Powerbuilder')
print str(horsemen)
print str(odbchelper)

print dir(li)
d={}
print dir(d)
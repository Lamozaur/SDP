#-*- coding: utf-8 -*
# 3.4 - 3.8
d = {"server":"mpilgrim","database":"master"}
d
print d
d["server"]
print d["server"]
d["database"] = "pubs"
print d["database"]
d["uid"] = "sa"
"""print d"""
a = {}
a
a["klucz"] = 'wartość'
a["klucz"] = 'inna wartość'
a["Klucz"] = 'jeszcze inna wartość'
a
"""print a"""
d["licznik"] = 3
print d
d[42]="douglas"
print d
del d[42]
print d
d.clear()
print d

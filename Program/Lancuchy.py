#-*- coding: utf-8 -*
# 2.3-3.3
import odbchelper
odbchelper.__name__
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__
import sys
sys.path
print sys.path
sys
print sys

def fib(n):
    print 'n =',n
    if n > 1:
        return n*fib(n-1)
    else:
        print 'koniec'
        return 1

fib(5)
text = "Nie za długi tekst"
print text
text2 = 'Kolejny napis, ale bez polskich liter'
text2
'Kolejny napis, ale bez polskich liter'
print text2
text3 = 'Długi tekst, \nktóry po przecinku znajduje się w następnej lini'
print text3
text4 = r'Tutaj znaki specjalne np. \n \t, czy też \x26 nie zostaną zinterpretowane'
print text4


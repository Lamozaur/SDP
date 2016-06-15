"""li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print [elem for elem in li if len(elem) > 1]
print [elem for elem in li if len(elem) !="b"]
print [elem for elem in li if li.count(elem)==1]"""

print 'a' or 'b'
print '' or 'b'
print '' or {} or ()

def sidefx():
    print "in sidefx()"
    return 1
print 'a' or sidefx()

a="first"
b="second"
print 1 and a or b
print 0 and a or b

def f(x):
    return x*2
print f(3)
g = lambda x: x*2
print g(3)

print (lambda x: x*2)(3)

s = "this is\na\ttest"
print s
print s.split()
print " ".join(s.split())


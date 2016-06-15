import os
li = ['a','b','e']
for s in li:
    print s
print "\n".join(li)

for i in range(5):
    print i

for k,v in os.environ.items():
    print"%s=%s" % (k,v)
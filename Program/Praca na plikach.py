f = open("D:\skills.txt","rb")
print f
print f.mode
print f.name
print f.tell()
print f.seek(-128,2)
print f.tell()
tagData = f.read(128)
"""print tagData"""
print f.tell()
f.closed
f.close()
print f
print f.closed

logfile = open('test.log','w')
logfile.write('udany test')
logfile.close()
print open('test.log').read()
logfile = open('test.log', 'a')
logfile.write('linia 2')
logfile.close()
print open('test.log').read()
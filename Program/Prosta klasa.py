import fileinfo
class Nicosc(object):
    pass
f = fileinfo.FileInfo("/music/_singles/kairo.mp3")
f.__class__
def leakmem():
    f=fileinfo.FileInfo('/music/_singles/kairo.mp3')
for i in range(100):
    leakmem()


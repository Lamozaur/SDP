class counter(object):
    count = 0
    def __init__(self):
        self.__class__.count += 1

print counter
c = counter()
print c.count
print counter.count
d = counter()
print d.count

import fileinfo
m = fileinfo.MP3FileInfo()
m.__parse("/music/_singles/kairo.mp3")

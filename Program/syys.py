import sys
import fileinfo
import os
import glob

from fileinfo import MP3FileInfo
print '\n'.join(sys.modules.keys())

print fileinfo
print sys.modules["fileinfo"]
print sys.modules[MP3FileInfo.__module__]

print os.listdir("c:\\Moje\\")
print glob.glob('c:\\Moje\\*.jpg')

def listDirectory(directory,fileExtList):
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList
                if os.path.splitext(f)[1] in fileExtList]
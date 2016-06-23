#-*- coding: utf-8 -*

import unittest
import urllib2
import re

html_content = urllib2.urlopen('http://www.rec-global.com/search?searchword=QA%20Engineer&ordering=newest&searchphrase=exact&limit=20').read()

#matches = re.findall('QA Engineer', html_content)
matches2 = re.findall('highlight',html_content)
ilosc = 0

if len(matches2) == 0:
   print 'Nic!'
else:
   ilosc = len(matches2)
   print 'Wystąpienia szukanego(zacieniowanego) tekstu',ilosc






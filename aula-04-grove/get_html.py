# -*- coding: latin-1 -*-

import urllib2
response = urllib2.urlopen("http://prc.ifsp.edu.br/")
page_source = response.read()

print page_source

#!/usr/bin/env python

import urllib
url =raw_input("Enter a URL:")
source = urllib.urlopen(url).read()
filename =raw_input("Filename: ")
file = open(filename, 'w')
file.write(source)
file.close()


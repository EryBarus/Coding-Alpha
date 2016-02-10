import re
import string
import urllib2
import time
import Tkinter 

class pack:
    def __init__(self, name, desc):
        self.n = name
        self.d = desc
    def display():
        print n + ':  ' + d 


def R_string (str_o) :
	st = str_o.replace("<td>", "").replace("<td>", "").replace("</td>", "").replace('&nbsp;', " ").replace('"', "").replace(">", "").replace("<", "").replace("/a", "")
	return st 

f = open ("out.txt", 'wb')
f.write (' ')
re1='">([0-9-A-z])([*-z])*.+<'
re2='<td>([0-9-A-z])(.)+'
rg1 = re.compile(re1,re.IGNORECASE|re.DOTALL)
rg2 = re.compile(re2,re.IGNORECASE|re.DOTALL)
url = urllib2.urlopen('https://pypi.python.org/pypi?%3Aaction=index')
html = url.readlines()
packages = []
q = ""
for line in html:
    s = ""
    r = ""
    j = 0
    k = 0
    i = 0
    i1 = 0
    m = rg1.search(line)
    m1 = rg2.search(line)
    if m and line[0:3] == " <t":
        j = 1
        word1=m.group(i)
        s = s+word1
        i+= 1
    s = R_string (s) 
    if m1 and line[0:4] == " <td":
        k = 1
        i1 = 0 
        word2=m1.group(i1)
        r = r+word2
        i1+= 1
    r = R_string (r) 
    if j is 1:
        q = ""
        q = s
    if k is 1:
        packages.append(pack(q, r))
    
for p in packages:
    print p.n + ':  ' + p.d + '\n'   

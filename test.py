import re
import string
import urllib.request
import urllib2


def R_string (str_o) :
	st = str_o.replace('&nbsp;', " ").replace('"', "").replace(">", "").replace("<", "").replace("/a", "")
	return st

def url_r (url, a)
	response = urllib2.urlopen(url) 
	l = []
	txt1 = ''
	for line in data.readlines():
		l.append(line)
	txt1= '\n'.join(l)
	if a is 1:
		return l
	else:
		return txt1 

t1 = url_r ('https://docs.python.org/2/bugs.html', 0)
txt=' <td><a href="https://pypi.python.org/pypi/AC-Flask-HipChat/0.2.2">AC-Flask-HipChat&nbsp;0.2.2</a></td>'

re1='">([*-z])*.+<'

i = 0
s = ""
rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
m = rg.search(t1)
if m:
    word1=m.group(i)
    s = s+word1
    i+= i

s = R_string (s)
print s 

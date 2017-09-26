#change this to your un/pn
user_name='your username'
pass_word='your password'

def py(s):
    if isinstance(s, unicode):
        return s.encode('ascii','ignore')
    else:
        return s.decode('utf-8','ignore').encode('ascii','ignore')

import re
fp=open("list.txt","r")
s=fp.readlines()
fp.close()
tmp=[]
#strip \n \r
for p in s:
    p=re.sub("\n","",p)
    p=re.sub("\r","",p)
    if len(p)>0:
        tmp.append(p)
s=tmp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import HTMLParser
html_parser=HTMLParser.HTMLParser()
def get_code(g):
    urllib.urlretrieve(g,'tmp.txt')
    fp=open('tmp.txt','r')
    s=''.join(fp.readlines())
    t1=s.find('<pre class="prettyprint linenums">')+len('<pre class="prettyprint linenums">')
    t2=s.find('</pre>')
    r=s[t1:t2]
    return html_parser.unescape(py(r))
driver=webdriver.Chrome()  #ChromeDriver Installation Required
driver.implicitly_wait(15)
driver.get("https://practice.contest.atcoder.jp/login")
driver.find_element_by_name('name').send_keys(user_name)
driver.find_element_by_name('password').send_keys(pass_word)
driver.find_element_by_tag_name('button').click()
for p in s:
    print 'processing '+p
    con=p[:6]
    id=p[-1:]
    if con[:3]=='arc':
        id=chr(ord(id)-2)
    url='https://'+con+'.contest.atcoder.jp/submissions/me?status=AC&task_screen_name='+con+'_'+id
    driver.get(url)
    driver.implicitly_wait(0)
    tbs=driver.find_elements_by_tag_name('table')
    driver.implicitly_wait(15)
    if len(tbs)<1:
        continue
    tb=tbs[0]
    rs=tb.find_elements_by_tag_name('tr')
    if len(rs)<2:
        continue
    print 'found code'
    g=rs[1].find_elements_by_tag_name('a')[1].get_attribute('href')
    fp=open(p+".cpp","w")
    fp.write(get_code(g))
    fp.close()
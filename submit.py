url='https://you_know_what.org/#!/' #edit it to right url
un='your username' #edit it to username
ps='your password' #edit it to password

from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
import time
import urllib
import HTMLParser
html_parser=HTMLParser.HTMLParser()
driver=webdriver.Chrome()  #ChromeDriver Installation Required
driver.implicitly_wait(8) #maybe you need to edit this according to your internet speed :)
driver.get(url)
#submit problem pn, using pn.cpp
#what is pascal? not exists.
def submit(pn,ct=0):
   try:
    pn=str(pn)
    if ct==3:
        return
    try:
        t=open(pn+'.cpp','r')
    except:
        return
    path=os.getcwd()+'\\'+pn+'.cpp'
    print 'Submitting '+pn+' Try '+str(ct)
    print path
    driver.get(url+'contest/23/problem/'+pn)
    sleep(1)
    ac=0
    t=driver.find_elements_by_class_name('label-success')
    for e in t:
        if e.get_attribute('innerHTML').find('Accepted')!=-1:
            ac=1
    if ac:
        print 'Accpted, ignored '+pn+'.'
        return
    se=driver.find_element_by_tag_name('select')
    ops=se.find_elements_by_tag_name('option')
    id=-1
    for g in range(0,len(ops)):
        r=ops[g].get_attribute('label').lower()
        if (r.find('g++')!=-1 or r.find('c++')!=-1) and r.find('11')!=-1:
            id=g
    if id==-1:
      for g in range(0,len(ops)):
        r=ops[g].get_attribute('label').lower()
        if (r.find('g++')!=-1 or r.find('c++')!=-1):
            id=g
    if id==-1:
        print "Error submitting "+pn+": cannot select proper language."
        submit(pn,ct+1)
        return
    ops[id].click()
    driver.find_element_by_id('answer').send_keys(path)
    sleep(1)
    driver.find_element_by_class_name('btn-success').click()
    sleep(1)
    print 'Submitted '+pn+' (probably)'
   except:
    return
#login
driver.find_element_by_class_name('dropdown-toggle').click()
driver.find_elements_by_tag_name('input')[0].send_keys(un)
driver.find_elements_by_tag_name('input')[1].send_keys(ps)
driver.find_element_by_class_name('btn-success').click()
for r in range(0,104):
    submit(r)

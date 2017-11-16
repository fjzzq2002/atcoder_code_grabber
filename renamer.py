import os
import shutil
t=open('list-unsorted.txt','r')
g=t.readlines()
cnt=0
for r in g:
    s=r
    s=s.replace('\n','')
    s=s.replace('\r','')
    if os.path.exists(s+'.cpp'):
        shutil.copy(s+'.cpp',str(cnt)+'.cpp')
    cnt=cnt+1
print cnt
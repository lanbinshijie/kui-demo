import time
from os import system
d = 0
try:
    with open("VERSION.SETTINGS.LSET",'r') as f:
        d = int(f.read())
except:
    pass
with open("VERSION.SETTINGS.LSET",'w') as f:
    f.write(str(d+1))

timea = time.strftime(f"%Y.%m.%d | %H:%M:%S | version => {d}", time.localtime())

system("git add .")
system("git commit -m \"" + timea + "\"")
system("git push")

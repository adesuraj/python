import re
co=0
p=re.compile('[a-z]')
p1=p.findall("aasurahhdkSGDhhdafffglabbb")
print(type(p1))

for i in p1:
    if i=='a' or 'b':
        co+=1
print(co)
print(len(p1))
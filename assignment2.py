def pattern(r,value=0):
    if r==0:
        global t
        return value
    else:
        return pattern((r-1),value+r)
p=pattern(5)
print(p)

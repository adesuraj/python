a=int(input("enter first number:"))
b=int(input("enter second number:"))
def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a
result=gcd(a,b)
print(result)
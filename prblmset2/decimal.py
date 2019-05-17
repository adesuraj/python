a=int(input("enter the number:"))
def bin(a):
    dec = 0
    power = 0
    while a > 0:
        dec =dec + 2 ** power * (a % 10)
        a //=10
        power += 1
    return dec
print("Decimal Number:", bin())


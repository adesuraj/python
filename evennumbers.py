list = []
class number:
    def __init__(self):
        size = input("Enter the size")
        print "Enter the numbers"
        for i in range(0,size):
            numbers = input()
            list.append(numbers)
    def checkEven(self, list):
        for i in list:
            if i % 2 == 0:
                return i
        raise ValueError("no numbers")
obj = number()
print "First Even number in list", obj.checkEven(list)



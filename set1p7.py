first_string=str(input("enter string one:"))
second_string=str(input("enter string two:"))

def isin(first_string,second_string):
    if (first_string in second_string)or(second_string in first_string):
        print("true")
    else:
        print("false")
isin(first_string,second_string)

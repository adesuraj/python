l=[]

no_range=int(input("enter no:"))
for i in range(0,no_range):
    user_odd_no=int(input("ENTER NO'S:"))
    if user_odd_no%2!=1:
        print("enter odd no's")
    else:
       l.append(user_odd_no)
max_odd_no=max(l)
print(max_odd_no)

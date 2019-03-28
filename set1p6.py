st=str(input("enter no:"))
stt=st.replace(","," ")
sttt=stt.split()
sum=0
list_of_nO=list(sttt)
for i in list_of_nO:
    sum=sum+float(i)
print(sum)

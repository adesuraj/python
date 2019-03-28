actual_cost=24.95
discount=40
shipping_charge=3
shipping_charge_after_one=0.75
cost=actual_cost*discount/100
b_cost=actual_cost-cost
display_total=0
print(b_cost)
no_of_copies=60
c=cost*59*0.75

while no_of_copies!=0:
    if no_of_copies==1:
        print("before adding",display_total)
        display_total=display_total+b_cost+shipping_charge
        print("after",display_total)

    else:
        display_total+=b_cost*shipping_charge_after_one
    no_of_copies-=1
print("total cost of 60 copies is:%d"%(display_total))


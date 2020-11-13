a=float(input("Enter sales amount: Rs."))
if (a<=20000.0):
    a=a-((10.0/100.0)*a)
elif(a>20000.0):
    a=a-((17.5/100.0)*a)
b=float(input("Enter sales tax payable(in %): "))
if (b>=5) and (b<=12):
    a=a+((b/100.0)*a)
    print ("Amount payable: Rs.",a)
else:
    print("The sales tax should be in the range 5 to 12%")

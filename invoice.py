c=int(input("Enter 1 to buy footwear,2 to buy garments and 3 for sports item: "))
if(c==1):
    i="Footwear"
    cp=float(input("Enter the cost price: Rs."))
    if (cp<=500):
        gstr=5
    else:
        gstr=18
elif(c==2):
    i="Garments"
    cp=float(input("Enter the cost price: Rs."))
    if (cp<=1000):
        gstr=5
    else:
        gstr=12
elif(c==3):
    i="Sports item"
    cp=float(input("Enter the cost price: Rs."))
    if (cp<5000):
        gstr=12
    else:
        gstr=18
else:
    print "Invalid choice"
print "\n\n\t\tINVOICE"
print "Item name: ",i
print "Cost price: Rs.",cp
print "GST rate: ",gstr,"%"
print "GST: Rs.",((gstr/100.0)*cp)
print "Selling Price: Rs.",(cp+((gstr/100.0)*cp))

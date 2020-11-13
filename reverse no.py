n=int(input("Enter a no. greater than 1000: "))
if(n>1000):
    n1=""
    while(n!=0):
        r=n%10
        n1+=str(r)
        n//=10
    print "Reverse no: ",n1
else:
    print ("Invalid input")

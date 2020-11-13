n=input("Enter a string: ")
for i in range(0,len(n),1):
    print (n[i]," ",n[-(i+1)])

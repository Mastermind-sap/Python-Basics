s=0;
for i in range(2,99):
    n=0
    for j in range(2,i):
        if(i%j==0):
            n=1;
            break;
    if (n==0):
        s+=i
print "Sum of prime nos. between 1 to 100:",s

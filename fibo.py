import fibo
a,b=0,1
n=0
while n<10:
    print (a," , ",b,end=' ')
    a=a+b
    b=a+b
    n+=1
print fibo(20)

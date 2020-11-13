a=int(input("Enter a integer: "))
b=int(input("Enter a integer: "))
c=int(input("Enter a integer: "))
if(a>b):
    if(a>c):
        print a," is the largest integer"
    elif(c>a):
        print c," is the largest integer"
elif(b>c):
    print b," is the largest integer"

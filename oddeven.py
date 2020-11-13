import random
c=input("Choose odd or even: ")
if (c!="odd" and c!="even"):
    print "Wrong choice"
else:
    a=random.randrange(7)
    b=int(input("Give your move: "))
    if(b>=7):
        raise IOError("Invalid input! You can give your move in the range 0 to 6 only")
    s=a+b
    if s%2==0:
        s1="even"
    else:
        s1="odd"
    if s1==c:
        c1=input("You won the toss,Choose bat or ball: ")
    else:
        c1=random.choice(["bat","ball"])
        print "you are ,",c1
    if c1=="bat":
        t=0
        o=0
        while(o==0):
            m=int(input("Give your move: "))
            if(m>=7):
                raise IOError("Invalid input! You can give your move in the range 0 to 6 only")
            z=random.randrange(7)
            if(m==z):
                print "You are out!"
                o=1
            else:
                t+=m
        print "You are balling and the cpu has a target of ",t+1
        co=0
        cs=0
        while (co==0 and cs<t+1):
             n=int(input("Give your ball: "))
             if(n>=7):
                raise IOError("Invalid input! You can give your move in the range 0 to 6 only")
             a=random.randrange(7)
             if(n==a):
                 print "the cpu is out and it made a score of",cs
                 co=1
             else:
                 cs+=a
                 print "Cpu scored:+ ",a
    elif c1=="ball":
        co=0
        cs=0
        while (co==0):
             n=int(input("Give your ball: "))
             if(n>=7):
                raise IOError("Invalid input! You can give your move in the range 0 to 6 only")
             a=random.randrange(7)
             if(n==a):
                 print "the cpu is out and it made a score of",cs
                 co=1
             else:
                 cs+=a
                 print "Cpu scored:+ ",a
        print "You are batting a target of ",cs+1
        t=0
        o=0
        while(o==0 and t<cs+1):
            m=int(input("Give your move: "))
            if(m>=7):
                raise IOError("Invalid input! You can give your move in the range 0 to 6 only")
            z=random.randrange(7)
            if(m==z):
                print "You are out!"
                o=1
            else:
                t+=m
    else:
        print ("Wrong choice")
    if(c1=="ball" or c1=="bat"):
        if t>cs:
            print "you won"
        elif cs>t:
            print "cpu won"
        elif cs==t:
            print "Its a draw"

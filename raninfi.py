import random
a=random.randrange(9)
b=int(input("Guess the no.: "))
if(a==b):
    print "You are right"
else:
    print "You are wrong, the no. was:",a

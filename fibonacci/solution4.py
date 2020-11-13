def getNthFib(n):
    a,b=0,1
    if n==1:
	return 0
    elif n==2:
	return 1
    elif n>2:
	for i in range(2,n):
		a,b=b,a+b
	return b
    pass

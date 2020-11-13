import sys
num=int(input("Enter number of matrices:"))
matrices=[]
for i in range(1,num+1):
    a=(eval(input("enter number "+str(i)+" matrice:")))
    rows=len(a)
    col=len(a[0])
    for j in a:
        if len(j)!=col:
            print("INVALID")
            sys.exit()
    matrices.append((a,(rows,col)))
order=matrices[0][1]
#print(order)
for k in matrices:
    if k[1]!=order:
        print("ADDITION NOT POSSIBLE")
        sys.exit()

res = [[0 for _ in range(order[1])] for p in range(order[0])]

for i in matrices:
    m=i[0]
    #print("m=",m)
    for j in range(order[0]):
        for k in range(order[1]):
            #print(j,k)
            #print("res1=",res[j][k])
            #print("elem",m[j][k])
            res[j][k]+=m[j][k]
            #print("res2",res[j][k])
            #for i in res:
            #    print(i)

print("The added matrix is:")            
for i in res:
    print(i)
#print (matrices)
            

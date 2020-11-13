import sys
num = int(input("Enter number of matrices:"))
matrices = []
for i in range(1, num+1):
    a = (eval(input("enter number "+str(i)+" matrice:")))
    rows = len(a)
    col = len(a[0])
    for j in a:
        if len(j) != col:
            print("INVALID")
            sys.exit()
    matrices.append((a, (rows, col)))
order = matrices[0][1]
print(order)
for k in matrices:
    if k[1] != order:
        sys.exit()
res = [[0 for _ in range(order[1])] for p in range(order[0])]

for i in matrices:
    m = i[0]
    for p in range(order[0]):  # No. of rows
        for q in range(order[1]):
            res[p][q] += m[p][q]

for i in res:
    print(i)

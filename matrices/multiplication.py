import sys
a = (eval(input("enter number first matrice:")))
b = (eval(input("enter number second matrice:")))
row_a=len(a)
col_a=len(a[0])
for j in a:
        if len(j) != col_a:
            print("INVALID MATRIX")
            sys.exit()
row_b=len(b)
col_b=len(b[0])
for j in b:
        if len(j) != col_b:
            print("INVALID MATRIX")
            sys.exit()
if col_a!=row_b:
    print("Cannot multiply")
    sys.exit()
res = [[1 for q in range(col_b)] for p in range(row_a)]



for m in range(row_a):
    

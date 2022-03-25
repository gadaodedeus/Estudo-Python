print ('\n\n\n\n')
n=int(input('n'))
m=int(input('m'))
aux=0
laux=[]
matrix=[]
for x in range(n):
    laux=[]
    for y in range(m):
        aux=int(input())
        laux.append(aux)
    
    matrix.append(laux)    
print(matrix)

for i in range(n):
    for j in range(m):
        print(matrix[i][j])

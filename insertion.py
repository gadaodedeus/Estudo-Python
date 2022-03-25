
print ('\n\n\n\n')
arquivo=open('arq.txt', "r")
lista=[]
for l in arquivo:
    lista.append(int(l))
print(lista)

valor=0; j=0
for i in range(len(lista)):
	valor=lista[i]
	j=i
	while j>0 and lista[j-1]>valor:
		lista[j]=lista[j-1]
		j-=1
	
	lista[j]=valor

print(lista)

output=open('ord.txt', 'w')
for i in range(len(lista)):
	output.write(str(lista[i]))
	output.write('\n')
output.close()
	

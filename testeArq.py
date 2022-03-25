print ('\n\n\n\n')
arquivo=open('arq.txt', "r")
lista=[]
for l in arquivo:
    lista.append(int(l))
print(lista)
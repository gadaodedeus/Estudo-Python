print ('\n\n\n\n')
laux=[]
lista=[]
dic={}
flag=1
while(flag):
    aux=str(input())
    laux=aux.split()
    lista.append(laux)
    flag=int(input('continue 1\\0?'))
print (lista)
dic=dict(lista)
print(dic)
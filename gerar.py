arquivo=open('arq.txt','w')
import random
qnt=10
for i in range(qnt):
    aux=str(random.randrange(qnt))
    arquivo.write(aux)
arquivo.close()
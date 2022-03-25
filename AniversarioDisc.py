print ('\n\n\n\n')
str1=str(input('data de nascimento:'))
meses={1:'janeiro', 2:'fevereiro', 3:'março', 4:'abril', 5:'maio', 6:'junho', 7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}
dia=int(str1[0]+str1[1])
m=int(str1[3]+str1[4])
mes=meses[m]
ano=int(str1[6]+str1[7]+str1[8]+str1[9])
print(dia, 'de', mes, 'de', ano)

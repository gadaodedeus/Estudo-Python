print ('\n\n\n\n')

print('-'*70)
print('\t\t\tAte 5 Kg\t\tAcima de 5Kg')
print('\t1-File Duplo\tR$ 4,90 por Kg\t\tR$ 5,80 por Kg')
print('\t2-Alcatra\tR$ 5,90 por Kg\t\tR$ 6,80 por Kg')
print('\t3-Picanha\tR$ 6,90 por Kg\t\tR$ 7,80 por Kg')
print('-'*70)
cd=int(input('Informe o codigo da carne desejada'))
qnt=float(input('Informe a quantidade de carne desejada'))

if(cd==1) & (qnt<=5.0):
    prec=4.9*qnt
elif(cd==1) & (qnt>5.0):
    prec=5.8*qnt
elif(cd==2) & (qnt<=5.0):
    prec=5.9*qnt
elif(cd==2) & (qnt>5.0):
    prec=6.8*qnt
elif(cd==3) & (qnt<=5.0):
    prec=6.9*qnt
elif(cd==3) & (qnt>5.0):
    prec=7.8*qnt
else:
    print('Codigo invalido!')
    prec=0.0
if prec:
    print('-'*50)
    print("\t\tPreço total:\tR$", '%.2f'%prec )
    print('-'*50)
    tp=str(input('Tipo do pagamento: '))
    if tp == 'cartao':
        card=str(input('Vai pagar com cartao Tabajara? S\\N'))
        if card == 'S':
            desc=0.05*prec
            print('-'*50)
            print('Desconto 5 por cento:\t%.2f'%desc)
            prec-=desc
    print('-'*50)
    print('Total a ser pago:\tR$ %.2f'%prec)
    print('-'*50)




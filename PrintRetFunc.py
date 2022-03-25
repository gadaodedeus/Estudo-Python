print ('\n\n\n\n')
#n=int(input())
def soma(l,c):
    while l>20:
        l=l//2
    while c>20:
        c=c//2
    for i in range(c):
        print('')
        for j in range(l):
            if i==0 or i==c-1 or j==0 or j==l-1:
                print ('@ ',end="")
            else:
                print('  ', end="")
soma(1000, 10)
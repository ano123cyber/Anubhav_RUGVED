<<<<<<< HEAD
def butterfly():
    N=int(input("Enter a number:"))
    for i in range(1,N+1): #Upper half
        for j in range(i):#For left half
            print('*',end=' ')
        for j in range(2*(N-i)):#For middle spaces
            print(' ',end=' ')
        for j in range(i):#For right half
            print('*',end=' ')
        print()
    for k in range(N-1,0,-1): #Lower half
        for l in range(k):#For left half
            print('*',end=' ')
        for l in range(2*(N-k)):#For middle spaces
            print(' ',end=' ')
        for l in range(k):#For right half
            print('*',end=' ')
        print()
butterfly()

=======
def butterfly():
    N=int(input("Enter a number:"))
    for i in range(1,N+1): #Upper half
        for j in range(i):
            print('*',end=' ')
        for j in range(2*(N-i)):
            print(' ',end=' ')
        for j in range(i):
            print('*',end=' ')
        print('\n')
butterfly()

>>>>>>> 0cdc8ead437185b27036fa68df9277ec1534e39a

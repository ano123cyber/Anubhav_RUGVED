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


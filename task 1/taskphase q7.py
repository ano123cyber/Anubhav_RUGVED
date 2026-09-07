def fibonacci():
    n=int(input("Enter number of terms:"))
    a=0
    b=1
    count=0
    for i in range(n):
        a, b=b, a+b
        count+=1
        print(a,end='')
fibonacci()
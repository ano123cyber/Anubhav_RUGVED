def fibonacci():
    n=int(input("Enter number of terms:"))
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c)
fibonacci()
def number():
    num=int(input("Enter a number:"))
    string=str(num)
    f=0
    valid=True
    for i in range(len(string)-1):
        if string[i]<=string[i+1]:
            if f==1 and string[i]<string[i+1]:
                valid=False
                break
        elif string[i]>=string[i+1]:
            if string[i]>string[i+1]:
                f=1
    if valid==True:
        print("Number is a hill number")
    else:
        print("Number is not a hill number")
number()
    
def is_valid():
    ccn=input("Enter a credit card number:")
    des=''.join(ccn.split())
    if not des.isdigit():
        return False
    totalsum=0
    reverse=des[::-1]
    index=0
    for digit in reverse:
        num=int(digit)
        if index%2==1:
            num=num*2
            if num>9:
                num=num-9
            index+=1
        totalsum=totalsum+num
    if totalsum%10==0:
        print("Credit card number is valid")
    else:
        print("Credit card number is invalid")
is_valid()
    

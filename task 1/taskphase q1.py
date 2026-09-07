def triple_and():
    a=input("Enter true or false for a:")
    b=input("Enter true or false for b:")
    c=input("Enter true or false for c:")
    if (a=="True" and b=="True" and c=="True"):
        return True
    else:
        return False
res=triple_and()
print(res)

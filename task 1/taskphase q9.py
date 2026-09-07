def caesar_cypher():
    message=input("Enter message to encrypt:")
    n=int(input("Enter value for change:"))
    list1=list(message)
    for i in range(len(list1)):
        if list1[i].isupper():
            startvalue=65
            startvalue=startvalue+(ord(list1[i]) - 65 + n) % 26
            list1[i]=chr(startvalue)
        if list1[i].islower():
            startvalue=97
            startvalue=startvalue+(ord(list1[i]) - 97 + n) % 26
            list1[i]=chr(startvalue)
    list2=''.join(list1)
    print("The encrypted message is:",list2)
caesar_cypher()
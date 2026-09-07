input_string=input("Enter a string:")
try:
    n=int(input("Enter number of characters per part:"))
    s=len(input_string)
    i=0
    if s%n!=0:
        print("Error in dividing string as remainder is not zero")
    else:
        first_part=input_string[0:n]
        for i in range(0,s,n):
            print(input_string[i:i+n])
            if first_part!=input_string[i:i+n]:
                print("Error in dividing string as first part is not equal to other parts")
                break
except ValueError:
    print("Please enter a valid integer for number of characters per part.")
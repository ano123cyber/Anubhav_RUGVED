def selection_sorter():
    string=input("Enter a string:")
    list1=list(string)
    n=len(list1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
    print("Sorted string is:",''.join(list1))
selection_sorter()
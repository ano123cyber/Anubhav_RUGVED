def umpires():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict1={}
    list1=[]
    for line in reader:
        umpire1=line[15]
        umpire2=line[16]
        if umpire1 in dict1:
            dict1[umpire1]+=1
        else:
            dict1[umpire1]=1
        if umpire2 in dict1:
            dict1[umpire2]+=1
        else:
            dict1[umpire2]=1
    list1.extend(list(dict1.values()))
    max1=max(list1)
    for umpire in dict1:
        if dict1[umpire]==max1:
            print("Umpire with maximum matches is:",umpire,"\nTotal matches:",max1)
    file.close()
umpires()
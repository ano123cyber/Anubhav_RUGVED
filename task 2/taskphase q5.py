def tiedornormal():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    tied_count=normal_count=0
    for line in reader:
        result=line[8]
        if result=='tie':
            tied_count+=1
        if result=='normal':
            normal_count+=1
    print("Number of tied matches:",tied_count)
    print("Number of normal matches:",normal_count)
    file.close()
tiedornormal()

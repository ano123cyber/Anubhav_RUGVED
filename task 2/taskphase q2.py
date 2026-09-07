def no_cities():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    city_count={}
    next(reader)
    for line in reader:
        city_name=line[2]
        if city_name in city_count:
            city_count[city_name]+=1
        else:
            city_count[city_name]=1
    for city in city_count:
        list1=list(city_count.values())
        for i in range(len(list1)):
            max1=max(list1)
            min1=min(list1)
        if city_count[city]==max1:
            print("City with maximum matches is:",city)
        if city_count[city]==min1:
            print("City with minimum matches is:",city)
    file.close()
no_cities()
        
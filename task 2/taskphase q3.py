def count_matches():
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
    print(city_count)
    file.close()
count_matches()
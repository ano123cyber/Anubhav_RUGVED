def playerofmatch():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    player_dict={}
    for line in reader:
        player=line[13]
        if player in player_dict:
            player_dict[player]+=1
        else:
            player_dict[player]=1
    if player_dict[player]>3:
        print("Player of the match is:",player,"with count:",player_dict[player])
    file.close()
playerofmatch()
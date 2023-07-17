players=[{"name":"Steve Smith","No. of Century":48,"No. of half century":50,"Wickets":64,"Hat-trick":5,"Batting":[100,89,264]},{"name":"Virat Kohli","No. of Century":75,"No. of half century":131,"Wickets":8,"Hat-trick":3,"Batting":[150,80,183]},{"name":"Sean Williams","No. of Century":12,"No. of half century":48,"Wickets":147,"Hat-trick":6,"Batting":[50,120,174]}]
def number(players):
    num=0
    for player in players:
        if player['No. of Century']>=10:
            num+=1
    return("Number of players:",num)   
        if player['Hat-trick']>5:
            player['name']
    return("Player more than 5 Hat-trick:",player['name'])   
    # return("Number of players:",num)
cricket=number(players)
print(cricket)

def hat(players):
    for player in players:
        if player['Hat-trick']>5:
            player['name']
    return("Player more than 5 Hat-trick:",player['name'])
hattrick=hat(players)
print(hattrick)

# High_score=[{"Name":"Steve Smith","Highest":264},{"Name":"Virat Kohli","Highest":183},{"Name":"Sean Willaims","Highest":174}]
def high(players):
    
    for player in players:
        b=0
        player['Battng']
        if b>c:
            b+=1
    return("highest:",b)
        
        
        
batting=high(players)
print(batting)

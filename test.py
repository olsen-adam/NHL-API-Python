import requests, time

# nhlwebsite = requests.get("https://api-web.nhle.com/v1/standings/now")
# standings = nhlwebsite.json()
# standings = standings['standings']
# place = 1
# print("%3s|%17s|%3s" % ("plc","Team Name","pnt") + "\n" + "-" * 25)
# for team in standings:
#     print("%3d|%17s|%3d"% (place,team["placeName"]['default'], team["points"]))
#     place += 1 
    
    
    
def main():
    teamAbv = input("Input Team Abr: ")
    try:
        nhlgames = requests.get("https://api-web.nhle.com/v1/club-schedule/"+ teamAbv.upper() + "/week/now")
    except Exception as E:
        print("Invalid Team Abreviation!")
        return
    
    teamSchedule = nhlgames.json()
    
    for game in teamSchedule['games']:
        print("%13s | %12s @ %12s | ID: %d" % (game['gameDate'],game['awayTeam']['placeName']['default'],game['homeTeam']['placeName']['default'],game['id']))
    


if __name__ == "__main__":
    main()
import requests
import numpy as np
import math
import pandas as pd

PLAYERS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/players.json")

EVENTS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/worldCup-final.json")


def get_players():
    """
    get the list of players
    """

    return requests.get(PLAYERS_URL).json()


def get_events():
    """
    get the list of events in the match
    """

    return requests.get(EVENTS_URL).json()


def main():
    events = get_events()
    players = get_players()

    player_timemean={}
    player_team={}
    player_name={}

    goodplayers=[]
    for player in players:
     timeline=[]
     eventdiff=[]
     player_name[player['playerId']]=player['name']
     for event in events:
      if player['playerId']==event['playerId']:
       player_team[player['playerId']]=event['teamId']
       #if event['teamId']=='Croatia': print(timeline)
       if event['matchPeriod']=='1H': timeline.append(event['eventSec'])
       if event['matchPeriod']=='2H': timeline.append(event['eventSec']+2700)
     #print(timeline)
     if (max(timeline)-min(timeline))/60>45.: 
       goodplayers.append(player['playerId'])
       for i in range(len(timeline)):
         if i!=0: eventdiff.append(timeline[i]-timeline[i-1])
       #print(timeline)
       #print(eventdiff)
       npdiff=np.array(eventdiff)
       #print(npdiff.mean())
       player_timemean[player['playerId']]=npdiff.mean()

    player_posmean={}
 
    #players with two events distance >45'
    #print(player_timemean)
   
    for playID in goodplayers:
      positions=[]
      for event in events:
        if event['playerId']==playID: positions=positions+[event['positions'][0]]
      xpos=[]
      ypos=[]
      for position in positions:
        xpos.append(position['x'])
        ypos.append(position['y'])
      #print(playID)
      npx=np.array(xpos)
      npy=np.array(ypos)
      #print(npx.mean())
      #print(npy.mean()) 
      distquad=0
      for position in positions:
        distquad=distquad+(npx.mean()-position['x'])**2+(npy.mean()-position['y'])**2
      #print(distquad/len(positions))
      #print(math.sqrt(distquad/len(positions)))
      player_posmean[playID]=[npx.mean(),npy.mean(),distquad/len(positions)] 
 
    #print(player_posmean)

    output=[] 
    for playID in goodplayers:
      player_f={}
      player_f['identificativo_calciatore']=playID
      player_f['nome_calciatore']=player_name[playID]
      player_f['squadra_calciatore']=player_team[playID]
      player_f['posizione_media_x']=player_posmean[playID][0]
      player_f['posizione_media_y']=player_posmean[playID][1]
      player_f['distanza_quadratica_media']=player_posmean[playID][2]
      player_f['tempo_medio_tra_eventi']=player_timemean[playID]
      output.append(player_f)   


    pd.DataFrame(output).to_csv('problema_1.csv', index=False)

if __name__ == "__main__":
    main()

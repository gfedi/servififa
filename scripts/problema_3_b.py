#!/usr/bin/python3

import requests
import pandas as pd
from numpy import array
import numpy as np

PLAYERS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/players.json")
EVENTS_URL = ("https://raw.githubusercontent.com/mesosbrodleto/"
              "soccerDataChallenge/master/worldCup-final.json")
ACCURATE_TAG = 1801


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


def position_to_cell(position):
    """
    get position in the 5X5 grid
    """

    x = position['x']
    y = position['y']
    if x <= 20:
        cell_x = 0
    elif x > 20 and x <= 40:
        cell_x = 1    
    elif x > 40 and x <= 60:
        cell_x = 2
    elif x > 60 and x <= 80:
        cell_x = 3
    elif x > 80:
        cell_x = 4
        
    if y <= 20:
        cell_y = 0
    elif y > 20 and y <= 40:
        cell_y = 1    
    elif y > 40 and y <= 60:
        cell_y = 2
    elif y > 60 and y <= 80:
        cell_y = 3
    elif y > 80:
        cell_y = 4

    return cell_x, cell_y


def check_event_in_the_cell(cell_position, x, y):
    """
    return a Booelan
    """

    if cell_position == (x, y):
        return True

    return False


def main():
    match = get_events()
    players = get_players()

    events = pd.DataFrame(
        match, columns=['teamId', 'playerId', 'tags', 'eventId', 'positions'])

    events['cell_positions'] = events['positions'].apply(
        lambda x: [position_to_cell(k) for k in x])

    unumteam1=[]
    unumteam2=[]
    bisteam1=[]
    bisteam2=[]
    terteam1=[]
    terteam2=[]
    quaterteam1=[]
    quaterteam2=[]

    firstteam=True
    for t in events['teamId'].unique():
        tot_events = len(events.loc[(events['teamId'] == t) & \
            (events['positions'].apply(lambda x: len(x) == 1))]) + 2 * len(
                events.loc[(events['teamId'] == t) & \
                    (events['positions'].apply(lambda x: len(x) == 2))])
        tot_accurate_passes = len(events.loc[(events['teamId'] == t) & \
            (events['eventId'] == 8) & \
                (events['tags'].apply(lambda x: {"id": ACCURATE_TAG} in x)) & \
                    (events['positions'].apply(lambda x: len(x) == 1))]) + \
                        2 * len(events.loc[(events['teamId'] == t) & \
                            (events['eventId'] == 8) & \
                                (events['tags'].apply(
                                    lambda x: {"id": ACCURATE_TAG} in x)) & \
                                        (events['positions'].apply(
                                            lambda x: len(x) == 2))])
        tot_shots = len(events.loc[(events['teamId'] == t) & \
            (events['eventId'] == 10) & (events['positions'].apply(
                lambda x: len(x) == 1))]) + 2 * len(
                    events.loc[(events['teamId'] == t) & \
                        (events['eventId'] == 10) & (events['positions'].apply(
                            lambda x: len(x) == 2))])
        tot_foul = len(events.loc[(events['teamId'] != t) & \
            (events['eventId'] == 2) & (events['positions'].apply(
                lambda x: len(x) == 1))]) + 2 * len(
                    events.loc[(events['teamId'] != t) & \
                        (events['eventId'] == 2) & (events['positions'].apply(
                            lambda x: len(x) == 2))])

        for x in range(5):
            unumtemp=[]
            bistemp=[]
            tertemp=[]
            quatertemp=[]
            for y in range(5):

                events_in_the_cell = len(events.loc[(events['teamId'] == t) & \
                    (events['cell_positions'].apply(
                        lambda k: check_event_in_the_cell(k[0], x, y)))])
                accurate_passes_in_the_cell = len(
                    events.loc[(events['teamId'] == t) & \
                        (events['eventId'] == 8) & \
                            (events['tags'].apply(
                                lambda x: {"id": ACCURATE_TAG} in x)) & \
                                    (events['cell_positions'].apply(
                                        lambda k: check_event_in_the_cell(
                                            k[0], x, y)))])
                shots_in_the_cell = len(
                    events.loc[(events['teamId'] == t) & \
                        (events['eventId'] == 10) & \
                            (events['cell_positions'].apply(
                                lambda k: check_event_in_the_cell(
                                    k[0], x, y)))])
                foul_in_the_cell = len(
                    events.loc[(events['teamId'] != t) & \
                        (events['eventId'] == 2) & \
                            (events['cell_positions'].apply(
                                lambda k: check_event_in_the_cell(
                                    k[0], x, y)))])
                unumtemp.append(events_in_the_cell/float(tot_events))
                bistemp.append(accurate_passes_in_the_cell/float(tot_accurate_passes))
                tertemp.append(shots_in_the_cell/float(tot_shots))
                quatertemp.append(foul_in_the_cell/float(tot_foul))
            if firstteam:
              unumteam1.append(unumtemp)
              bisteam1.append(bistemp)
              terteam1.append(tertemp)
              quaterteam1.append(quatertemp)
            else:
              unumteam2.append(unumtemp)
              bisteam2.append(bistemp)
              terteam2.append(tertemp)
              quaterteam2.append(quatertemp)
        firstteam=False

    #print(bisteam1,bisteam2)    
    #print(terteam1,terteam2)    
    #print(quaterteam1,quaterteam2)    

    npunum1 =  np.array(unumteam1)
    npunum2 =  np.array(unumteam2)
    npbis1 =  np.array(bisteam1)
    npbis2 =  np.array(bisteam2)
    npter1 =  np.array(terteam1)
    npter2 =  np.array(terteam2)
    npquater1 =  np.array(quaterteam1)
    npquater2 =  np.array(quaterteam2)
    simil0=np.linalg.norm(np.multiply(npunum1,npunum2))/np.linalg.norm(npunum1)/np.linalg.norm(npunum2)
    simil1=np.linalg.norm(np.multiply(npbis1,npbis2))/np.linalg.norm(npbis1)/np.linalg.norm(npbis2)
    simil2=np.linalg.norm(np.multiply(npter1,npter2))/np.linalg.norm(npter1)/np.linalg.norm(npter2)
    simil3=np.linalg.norm(np.multiply(npquater1,npquater2))/np.linalg.norm(npquater1)/np.linalg.norm(npquater2)

    results_f=[{'tipo_griglia':'frequenza_eventi','similarity':simil0},{'tipo_griglia':'frequenza_passaggi_accurati','similarity':simil1},{'tipo_griglia':'frequenza_tiri','similarity':simil2},{'tipo_griglia':'frequenza_falli_subiti','similarity':simil3}] 


    pd.DataFrame(results_f).to_csv('problema_3_b.csv', index=False)


if __name__ == "__main__":
    main()

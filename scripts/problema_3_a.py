#!/usr/bin/python3

import requests
import pandas as pd
from numpy import array


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


def position_to_cell(positions):
    """
    get position in the 5X5 grid
    """

    x = positions['x']
    y = positions['y']
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


def main():
    match = get_events()
    players = get_players()

    events = pd.DataFrame(
        match, columns=['teamId', 'playerId', 'tags', 'eventId', 'positions'])


if __name__ == "__main__":
    main()

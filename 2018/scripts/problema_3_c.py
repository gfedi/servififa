#!/usr/bin/python3

import requests
import pandas as pd
import numpy as np


PLAYERS_URL = (
    "https://raw.githubusercontent.com/mesosbrodleto/"
    "soccerDataChallenge/master/players.json"
)
EVENTS_URL = (
    "https://raw.githubusercontent.com/mesosbrodleto/"
    "soccerDataChallenge/master/worldCup-final.json"
)
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

    x = position["x"]
    y = position["y"]
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
        match, columns=["teamId", "playerId", "tags", "eventId", "positions"]
    )

    events["cell_positions"] = events["positions"].apply(
        lambda x: [position_to_cell(k) for k in x]
    )

    team = {}
    for t in events["teamId"].unique():
        tot_events = len(events.loc[(events["teamId"] == t)])
        tot_accurate_passes = len(
            events.loc[
                (events["teamId"] == t)
                & (events["eventId"] == 8)
                & (events["tags"].apply(lambda x: {"id": ACCURATE_TAG} in x))
            ]
        )
        tot_shots = len(events.loc[(events["teamId"] == t) & (events["eventId"] == 10)])
        tot_foul = len(events.loc[(events["teamId"] != t) & (events["eventId"] == 2)])

        frequenza_eventi = np.matrix(5 * [5 * [0.]])
        frequenza_passaggi_accurati = np.matrix(5 * [5 * [0.]])
        frequenza_tiri = np.matrix(5 * [5 * [0.]])
        frequenza_falli_subiti = np.matrix(5 * [5 * [0.]])
        for x in range(5):
            for y in range(5):
                events_in_the_cell = len(
                    events.loc[
                        (events["teamId"] == t)
                        & (
                            events["cell_positions"].apply(
                                lambda k: check_event_in_the_cell(k[0], x, y)
                            )
                        )
                    ]
                )
                accurate_passes_in_the_cell = len(
                    events.loc[
                        (events["teamId"] == t)
                        & (events["eventId"] == 8)
                        & (events["tags"].apply(lambda x: {"id": ACCURATE_TAG} in x))
                        & (
                            events["cell_positions"].apply(
                                lambda k: check_event_in_the_cell(k[0], x, y)
                            )
                        )
                    ]
                )
                shots_in_the_cell = len(
                    events.loc[
                        (events["teamId"] == t)
                        & (events["eventId"] == 10)
                        & (
                            events["cell_positions"].apply(
                                lambda k: check_event_in_the_cell(k[0], x, y)
                            )
                        )
                    ]
                )
                foul_in_the_cell = len(
                    events.loc[
                        (events["teamId"] != t)
                        & (events["eventId"] == 2)
                        & (
                            events["cell_positions"].apply(
                                lambda k: check_event_in_the_cell(k[0], x, y)
                            )
                        )
                    ]
                )

                frequenza_eventi[x, y] = events_in_the_cell / float(tot_events)

                frequenza_passaggi_accurati[x, y] = accurate_passes_in_the_cell / float(
                    tot_accurate_passes
                )

                frequenza_tiri[x, y] = shots_in_the_cell / float(tot_shots)

                frequenza_falli_subiti[x, y] = foul_in_the_cell / float(tot_foul)

        team[t] = {
            "frequenza_eventi": frequenza_eventi,
            "frequenza_passaggi_accurati": frequenza_passaggi_accurati,
            "frequenza_tiri": frequenza_tiri,
            "frequenza_falli_subiti": frequenza_falli_subiti,
        }

    results = []
    for tipo_griglia in [
        "frequenza_eventi",
        "frequenza_passaggi_accurati",
        "frequenza_tiri",
        "frequenza_falli_subiti",
    ]:
        for x in range(5):
            for y in range(5):
                temp = {}
                temp["tipo_griglia"] = tipo_griglia
                temp["numero_cella_x"] = x
                temp["numero_cella_y"] = y
                temp["differenza_di_frequenza"] = abs(
                    team[events["teamId"].unique()[0]][tipo_griglia][x, y]
                    - team[events["teamId"].unique()[1]][tipo_griglia][x, y]
                )
                temp["squadra_dominante"] = (
                    events["teamId"].unique()[0]
                    if team[events["teamId"].unique()[0]][tipo_griglia][x, y]
                    > team[events["teamId"].unique()[1]][tipo_griglia][x, y]
                    else events["teamId"].unique()[1]
                )
                results.append(temp)

    pd.DataFrame(results).to_csv("problema_3_c.csv", index=False)


if __name__ == "__main__":
    main()

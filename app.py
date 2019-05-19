import constants
from copy import deepcopy

teams_list = constants.TEAMS
players_list = deepcopy(constants.PLAYERS)


def clean_data():
    for player in players_list:
        player['guardians'] = player['guardians'].split(' and ')
        player['experience'] = True if player['experience'] == 'YES' else False
        player['height'] = int(player['height'][:2])
    return players_list


def balance_team():
    pass


if __name__ == '__main__':
    clean_data()

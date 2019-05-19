import constants
from copy import deepcopy

teams_list = constants.TEAMS
players_list = deepcopy(constants.PLAYERS)


def clean_data(players):
    for player in players:
        player['guardians'] = player['guardians'].split(' and ')
        player['experience'] = True if player['experience'] == 'YES' else False
        player['height'] = int(player['height'][:2])
    return players_list


def split_experience_level(players):
    experienced = []
    inexperienced = []

    for player in players:
        if player['experience'] is True:
            experienced.append(player)
        else:
            inexperienced.append(player)
    return experienced, inexperienced


def balance_team(teams, players):
    experienced, inexperienced = split_experience_level(players)
    experience_split_value = len(experienced) // len(teams)
    panthers, bandits, warriors = [], [], []
    roster_list = [panthers, bandits, warriors]

    for index, player in enumerate(experienced):
        if index < experience_split_value:
            panthers.append(player)
        if (index >= experience_split_value and
                index < experience_split_value * 2):
            bandits.append(player)
        if index >= experience_split_value * 2:
            warriors.append(player)

    for index, player in enumerate(inexperienced):
        if index < experience_split_value:
            panthers.append(player)
        if (index >= experience_split_value and
                index < experience_split_value * 2):
            bandits.append(player)
        if index >= experience_split_value * 2:
            warriors.append(player)

    teams_dict = {team: roster_list[index] for index, team in enumerate(teams)}

    return teams_dict


def display_stats():
    pass


if __name__ == '__main__':
    split_experience_level(clean_data(players_list))
    balance_team(teams_list, players_list)

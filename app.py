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


def display_stats(team, teams_dict):
    print(f'\n Team: {team} Stats \n')
    print('-' * 30)
    print(f'\n Total number of players: {len(teams_dict[team])} \n')
    print('Roster:')

    # Print team roster
    for index, player in enumerate(teams_dict[team]):
        if index != len(teams_dict[team]) - 1:
            print(player['name'], end=', ')
        else:
            print(player['name'], '\n')

    # Create experienced, inexperienced roster list
    experienced = [player['name'] for player in teams_dict[team]
                   if player['experience'] is True]

    inexperienced = [player['name'] for player in teams_dict[team]
                     if player['experience'] is not True]

    # Print num of experienced players
    print(f'Total number of experienced players: {len(experienced)} \n')
    print('Experienced players:')

    # Print experienced player names
    for index, name in enumerate(experienced):
        if index != len(experienced) - 1:
            print(name, end=', ')
        else:
            print(name, '\n')

    # Print num of inexperienced players
    print(f'Total number of inexperienced players: {len(inexperienced)} \n')
    print('Inexperienced players:')

    # Print experienced player names
    for index, name in enumerate(inexperienced):
        if index != len(inexperienced) - 1:
            print(name, end=', ')
        else:
            print(name, '\n')

    # Calculate average height of team
    team_height = [player['height'] for player in teams_dict[team]]
    average_team_height = sum(team_height) / len(teams_dict[team])
    feet = average_team_height // 12
    inches = average_team_height % 12

    # Print average height of team
    print(f'Average height of the team: {feet:g} ft {inches} in \n')

    # Create guardians list
    guardians = [player['guardians'] for player in teams_dict[team]]

    # Print guardians of team
    print('Guardians:')
    for index, guardian in enumerate(guardians):
        for name_index, name in enumerate(guardian):
            if index == len(guardians) - 1:
                if name_index == len(guardian) - 1:
                    print(name, '\n')
                else:
                    print(name, end=', ')
            else:
                print(name, end=', ')

    print('\n Press ENTER to continue... \n')


if __name__ == '__main__':
    split_experience_level(clean_data(players_list))
    display_stats('Panthers', balance_team(teams_list, players_list))

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


def split_experience_level(players_list):
    experienced = []
    inexperienced = []

    for player in players_list:
        if player['experience'] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)
    return experienced, inexperienced


# def balance_team(teams_list, players_list):
#     total_num_teams = len(teams_list)
#     total_num_players = len(players_list)
#     team_split = total_num_players // total_num_teams
#     team_dict = {}

#     for index, player in enumerate(players_list):
#         if index 
#     print(team_dict)






    


if __name__ == '__main__':
    clean_data()
    split_experience_level(players_list)
    # balance_team(teams_list, players_list)

from constants import TEAMS, PLAYERS
from os import system, name, sys

teams_list = TEAMS
players_list = PLAYERS
main_menu_options = {1: 'Display Team Stats', 2: 'Quit'}
team_menu_options = {1: 'Panthers', 2: 'Bandits', 3: 'Warriors'}
navigation_menu_options = {1: 'Main Menu', 2: 'Team Menu', 3: 'Quit'}


def clean_data(players):
    players_list = []

    for player in players:
        player_dict = {}
        player_dict['name'] = player['name']
        player_dict['guardians'] = player['guardians'].split(' and ')
        player_dict['experience'] = (True if player['experience'] == 'YES'
                                     else False)
        player_dict['height'] = int(player['height'][:2])
        players_list.append(player_dict)
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


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def print_team_roster(team, teams_dict):
    print(f'\nTeam: {team}\n')
    print('-' * 30)
    print(f'\nTotal number of players: {len(teams_dict[team])} \n')
    print('Roster:')

    for index, player in enumerate(teams_dict[team]):
        if index != len(teams_dict[team]) - 1:
            print(player['name'], end=', ')
        else:
            print(player['name'], '\n')


def print_roster_by_experience_level(experienced, inexperienced):
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


def print_guardian_list(team, teams_dict):
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


def average_team_height(team, teams_dict):
    team_height = [player['height'] for player in teams_dict[team]]
    average_team_height = sum(team_height) / len(teams_dict[team])
    feet = round(average_team_height // 12)
    inches = round(average_team_height % 12)

    # Print average height of team
    print(f'Average height of the team: {feet} ft {inches} in \n')


def display_stats(team, teams_dict):
    # Print team roster stats
    print_team_roster(team, teams_dict)

    # Create experienced, inexperienced lists
    experienced = [player['name'] for player in teams_dict[team]
                   if player['experience'] is True]

    inexperienced = [player['name'] for player in teams_dict[team]
                     if player['experience'] is not True]

    # Print num of experienced players
    print_roster_by_experience_level(experienced, inexperienced)

    # Calculate average height of team
    average_team_height(team, teams_dict)

    # Print guardians of team
    print_guardian_list(team, teams_dict)

    print('-' * 30)


def welcome_message():
    welcome_message = ' BASKETBALL TEAM STATS TOOL '
    print('#' * (len(welcome_message) + 2))
    print(f'#{welcome_message}#')
    print('#' * (len(welcome_message) + 2))


def menu_display(active_menu):
    if active_menu == 1:
        print('\n---- MAIN MENU ----\n')
        print('Selection Options:')
        for key, value in main_menu_options.items():
            print(f' {key}) {value}')
    elif active_menu == 2:
        print('\n---- TEAM MENU ----\n')
        print('Select Team:')
        for key, value in team_menu_options.items():
            print(f' {key}) {value}')
    elif active_menu == 3:
        print('\n---- NAVIGATION MENU ----\n')
        print('Selection Options:')
        for key, value in navigation_menu_options.items():
            print(f'{key}) {value}')


def get_user_input(active_menu):
    user_input = ''

    if active_menu == 1:
        try:
            print('\n')
            user_input = int(input('Enter an option > '))
            if user_input not in main_menu_options.keys():
                raise ValueError
            return user_input
        except ValueError:
            print('\n** Invalid input. Please enter a numeric option. **\n')
            menu_display(active_menu)
    elif active_menu == 2:
        try:
            print('\n')
            user_input = int(input('Enter an option > '))
            if user_input not in team_menu_options.keys():
                raise ValueError
            return user_input
        except ValueError:
            print('\n** Invalid input. Please enter a numeric option. **\n')
            menu_display(active_menu)
    elif active_menu == 3:
        try:
            print('\n')
            user_input = int(input('\n Enter an option > '))
            if user_input not in navigation_menu_options.keys():
                raise ValueError
            return user_input
        except ValueError:
            print('Invalid input. Please enter a numeric option.')
            menu_display(active_menu)


def main(active_menu=1):
    menu_display(active_menu)

    while active_menu == 1:
        choice = get_user_input(active_menu)

        if choice is None:
            continue
        else:
            if choice == 1:
                active_menu = 2
                clear_screen()
                menu_display(active_menu)
            elif choice == 2:
                clear_screen()
                sys.exit()

    while active_menu == 2:
        choice = get_user_input(active_menu)

        if choice is None:
            continue
        else:
            clear_screen()
            display_stats(team_menu_options[choice], roster)
            active_menu = 3
            menu_display(active_menu)

    while active_menu == 3:
        choice = get_user_input(active_menu)

        if choice is None:
            continue
        else:
            if choice == 1:
                clear_screen()
                main(active_menu=1)
            elif choice == 2:
                clear_screen()
                main(active_menu=2)
            elif choice == 3:
                clear_screen()
                sys.exit()


if __name__ == '__main__':
    clear_screen()
    welcome_message()
    data = clean_data(players_list)  # Clean data
    roster = balance_team(teams_list, data)  # Create roster
    main()

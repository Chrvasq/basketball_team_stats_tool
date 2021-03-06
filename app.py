#!/usr/bin/env python3

from constants import TEAMS, PLAYERS
from os import system, name, sys

# ANSI escape sequence variables to add color
GREEN = '\033[1;92m'  # Bold and green
YELLOW = '\033[1;93m'  # Bold and yellow
RED = '\033[1;91m'  # Bold and red
UNDERLINE = '\033[4m'  # Add underline
END = '\033[0m'  # Reset formatting

teams_list = TEAMS
players_list = PLAYERS
main_menu_options = {1: 'Display Team Stats', 2: 'Quit'}
team_menu_options = {1: 'Panthers', 2: 'Bandits', 3: 'Warriors'}
navigation_menu_options = {1: 'Main Menu', 2: 'Team Menu', 3: 'Quit'}


def clean_data(players):
    """Creates a new dictionary and performs data transformations
    
    Arguments:
        players {list} -- list of dictionaries with player information
    
    Returns:
        dict -- dictionary with transformed data values
    """
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
    """Creates two lists based on experience level
    
    Arguments:
        players {list} -- list of dictionaries with player information
    
    Returns:
        list -- lists of experienced/inexperienced players
    """
    experienced = []
    inexperienced = []

    for player in players:
        if player['experience'] is True:
            experienced.append(player)
        else:
            inexperienced.append(player)
    return experienced, inexperienced


def balance_team(teams, players):
    """Creates a new dictionary with player roster split by experience level
    
    Arguments:
        teams {list} -- list of teams
        players {list} -- list of dictionaries with player information
    
    Returns:
        [type] -- [description]
    """
    experienced, inexperienced = split_experience_level(players)
    team_list = [[] for _ in range(len(teams))]

    for index, player in enumerate(experienced):
        team_number = index % len(teams)
        team_list[team_number].append(player)

    for index, player in enumerate(inexperienced):
        team_number = index % len(teams)
        team_list[team_number].append(player)

    teams_dict = {team: team_list[index] for index, team in enumerate(teams)}

    return teams_dict


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def print_team_roster(team, teams_dict):
    """Prints team roster
    
    Arguments:
        team {str} -- team name
        teams_dict {dict} -- dictionary of player information
    """
    print('\nTeam: ' + GREEN + f'{team}\n' + END)
    print(RED + '-' * 30 + END)
    print(f'\nTotal number of players: {len(teams_dict[team])} \n')
    print('Roster:')

    for index, player in enumerate(teams_dict[team]):
        if index != len(teams_dict[team]) - 1:
            print(player['name'], end=', ')
        else:
            print(player['name'], '\n')


def print_roster_by_experience_level(experienced, inexperienced):
    """Prints player names by experience level
    
    Arguments:
        experienced {list} -- list of experienced players
        inexperienced {list} -- list of inexperienced players
    """
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
    """Prints guardians of players
    
    Arguments:
        team {str} -- team name
        teams_dict {dict} -- dictionary of player information
    """
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
    """Calculates and prints average team height
    
    Arguments:
        team {str} -- team name
        teams_dict {dict} -- dictionary of player information
    """
    team_height = [player['height'] for player in teams_dict[team]]
    average_team_height = sum(team_height) / len(teams_dict[team])
    feet = round(average_team_height // 12)
    inches = round(average_team_height % 12)

    # Print average height of team
    print(f'Average height of the team: {feet} ft {inches} in \n')


def display_stats(team, teams_dict):
    """Displays team stats based on team name
    
    Arguments:
        team {str} -- team name
        teams_dict {dict} -- dictionary of player information
    """
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

    print(RED + '-' * 30 + END)


def welcome_message():
    welcome_message = ' BASKETBALL TEAM STATS TOOL '
    print('#' * (len(welcome_message) + 2))
    print(f'#{welcome_message}#')
    print('#' * (len(welcome_message) + 2))


def menu_display(active_menu):
    """Determines which menu to display
    
    Arguments:
        active_menu {int} -- integer between 1 and 3
    """
    if active_menu == 1:
        print(YELLOW + '\n---- MAIN MENU ----\n' + END)
        print(UNDERLINE + 'Selection Options:' + END)
        for key, value in main_menu_options.items():
            print(f' {key}) {value}')
    elif active_menu == 2:
        print(RED + '\n---- TEAM MENU ----\n' + END)
        print(UNDERLINE + 'Select Team:' + END)
        for key, value in team_menu_options.items():
            print(f' {key}) {value}')
    elif active_menu == 3:
        print(GREEN + '\n---- NAVIGATION MENU ----\n' + END)
        print(UNDERLINE + 'Select Menu:' + END)
        for key, value in navigation_menu_options.items():
            print(f'{key}) {value}')


def get_user_input(active_menu):
    """Prompts user for input
    
    Arguments:
        active_menu {int} -- integer between 1 and 3
    
    Raises:
        ValueError: user_input not in menu options
        ValueError: user_input not in menu options
        ValueError: user_input not in menu options
    
    Returns:
        int -- integer based on menu option
    """
    user_input = ''
    error_message = '\n** Invalid input. Please enter a numeric option. **\n'
    error_message = YELLOW + error_message + END  # Add formatting to message
    prompt = YELLOW + 'Enter an option > ' + END

    if active_menu == 1:
        try:
            print('\n')
            user_input = int(input(prompt))
            if user_input not in main_menu_options.keys():
                raise ValueError
            return user_input
        except ValueError:
            print(error_message)
            menu_display(active_menu)
    elif active_menu == 2:
        try:
            print('\n')
            user_input = int(input(prompt))
            if user_input not in team_menu_options.keys():
                raise ValueError
            return user_input
        except ValueError:
            print(error_message)
            menu_display(active_menu)
    elif active_menu == 3:
        try:
            print('\n')
            user_input = int(input(prompt))
            if user_input not in navigation_menu_options.keys():
                raise ValueError
            return user_input
        except ValueError:
            print(error_message)
            menu_display(active_menu)


def main(active_menu=1):
    """Main function that handles main loop
    
    Keyword Arguments:
        active_menu {int} -- integer bwteeen 1 and 3 (default: {1})
    """
    menu_display(active_menu)
    running = True

    while running:
        choice = get_user_input(active_menu)

        if choice is None:
            continue

        if active_menu == 1:
            if choice == 1:
                clear_screen()
                main(active_menu=2)
            elif choice == 2:
                clear_screen()
                sys.exit()
        elif active_menu == 2:
            clear_screen()
            display_stats(team_menu_options[choice], roster)
            main(active_menu=3)
        elif active_menu == 3:
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

def players():
    players_dict = {
        'player_x' : input('Add a name for player X:'),
        'player_o' : input('Add a name for player O:'),
    }
    return players_dict

def validator():
    is_valid = False    
    players_dict = players()

    while not is_valid:
        if not players_dict['player_o'] or not players_dict['player_x']:
            print("The players name can't contain blanks")
            players_dict = players()
        elif ' ' in players_dict['player_x'] or ' ' in players_dict['player_o']:
            print("The players name can't contain blanks")
            players_dict = players()
        elif players_dict['player_x'] == players_dict['player_o']:
            print("The players name can't be the same")
            players_dict = players()
        elif players_dict['player_x'].isnumeric() or players_dict['player_o'].isnumeric():
            print("The players name can't have just numbers")
            players_dict = players()
        else:
            is_valid = True

    return players_dict

def handle_players_movements(player_name):
    players_xo_move = {}
    player_movements = input(player_name +', enter your movement:')
    is_valid = False

    while not is_valid:
        if not player_movements.isnumeric() or len(player_movements) > 1 or player_movements == '0':
            print('only numbers from 1 to 9 are allowed')
            player_movements = input(player_name +', enter your movement:')
        else:
            is_valid = True

    if player_name not in players_xo_move:
        players_xo_move[player_name] = [player_movements]
    else:
        players_xo_move[player_name].append(player_movements)

    return players_xo_move

def layout():
    x = ["1","2","3"]
    y = ["4","5","6"]
    z = ["7","8","9"]

    print(x)
    print(y)
    print(z)

def main():
    named_players = validator()
    handle_players_movements(named_players['player_x'])
    handle_players_movements(named_players['player_o'])
    layout()

main()

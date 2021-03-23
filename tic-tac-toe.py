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
    
def layout():
    x = ["_","_","_"]
    y = ["_","_","_"]
    z = ["_","_","_"]

    print(x)
    print(y)
    print(z)

def main():
    named_players = validator()
    layout()

main()

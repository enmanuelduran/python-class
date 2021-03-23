def players():
    players_dict = {
        'player_x' : input('Add a name for player X: '),
        'player_o' : input('Add a name for player O: '),
    }
    return players_dict

def validator():
    players_dict = players()

    if players_dict['player_x'] == players_dict['player_o']:
        print("The players name can't be the same")
        players_dict = players()
    if players_dict['player_x'].isnumeric() or players_dict['player_o'].isnumeric():
        print("The players name can't have numbers")
        players_dict = players()
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

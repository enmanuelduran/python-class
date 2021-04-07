players_xo_move = {}

player_x_movement = input('Player X, enter your movement:')

while 'player_x_movement' not in players_xo_move:
    if not player_x_movement.isnumeric() or len(player_x_movement) > 1 or player_x_movement == '0':
        print('only numbers from 1 to 9 are allowed')
        player_x_movement = input('Player X, enter your movement:')
    else:
        players_xo_move['player_x_movement'] = player_x_movement


player_o_movement = input('Player O, enter your movement:')

while 'player_o_movement' not in players_xo_move:
    if not player_o_movement.isnumeric() or len(player_o_movement) > 1 or player_o_movement == '0':
        print('only numbers from 1 to 9 are allowed')
        player_o_movement = input('Player O, enter your movement:')
    else:
        players_xo_move['player_o_movement'] = player_o_movement


print(players_xo_move)


import pprint

pp = pprint.PrettyPrinter(width=18, compact=True)


play_board = ["1","2","3","4","5","6","7","8","9"]

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

is_valid = False
while not is_valid:
    player_x_moved = handle_players_movements('kike')
    for movements in play_board:
        if movements in player_x_moved['kike']:
            print('')
            play_board[int(movements) - 1] = 'X'
            pp.pprint(play_board)
            print('\n Next play\n')

    player_o_moved = handle_players_movements('maco')
    for movements in play_board:
        if movements in player_o_moved['maco']:
            print('')
            play_board[int(movements) - 1] = 'O'
            pp.pprint(play_board)
            print('\n Next play\n')


        




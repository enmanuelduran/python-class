import pprint
from datetime import datetime
import winsound


pp = pprint.PrettyPrinter(width=18, compact=True)

def players():
    players_dict = {
        'X' : input('Add a name for player X:'),
        'O' : input('Add a name for player O:'),
    }
    return players_dict

def validator():
    is_valid = False    
    players_dict = players()

    while not is_valid:
        if not players_dict['O'] or not players_dict['X']:
            print("The players name can't contain blanks")
            players_dict = players()
        elif ' ' in players_dict['X'] or ' ' in players_dict['O']:
            print("The players name can't contain blanks")
            players_dict = players()
        elif players_dict['X'] == players_dict['O']:
            print("The players name can't be the same")
            players_dict = players()
        elif players_dict['X'].isnumeric() or players_dict['O'].isnumeric():
            print("The players name can't have just numbers")
            players_dict = players()
        else:
            is_valid = True

    return players_dict

def handle_players_movements(player_name, table):
    players_xo_move = {}
    player_movements = input(player_name +', enter your movement:')
    is_valid = False

    while not is_valid:
        if (
            not player_movements.isnumeric() 
            or len(player_movements) > 1 
            or player_movements == '0'   
        ):
            print('only numbers from 1 to 9 are allowed')
            player_movements = input(player_name +', enter your movement:')
        elif not player_movements in table:
            print('this position is already filled')
            player_movements = input(player_name +', enter your movement:')
        else:
            is_valid = True

    if player_name not in players_xo_move:
        players_xo_move[player_name] = [int(player_movements)]
    else:
        players_xo_move[player_name].append(int(player_movements))

    return players_xo_move

def render_movement(table, player_sign, player_movements):
    print('')
    last_movement=player_movements[-1]
    table[last_movement-1]= player_sign
    pp.pprint(table)
    print('\n Next play\n')

def report_winners(table):
    return (
        #Horizontals
        table[0]==table[1]==table[2]  
        or table[3]==table[4]==table[5] 
        or table[6]==table[7]==table[8] 
        #Verticals
        or table[0]==table[3]==table[6]
        or table[1]==table[4]==table[7]
        or table[2]==table[5]==table[8]
        #Diagonals
        or table[0]==table[4]==table[8]
        or table[2]==table[4]==table[6]
    )
       
def report_draw(table):
    count=0
    for elements in table:
        if not elements.isnumeric():
            count+=1
    
    if count==9:
        print('#___DRAW___#')
        return True        

def layout():
    table = ['1','2','3','4','5','6','7','8','9']
    return table

def time_per_play(now):
        later = datetime.now()
        time = later.second - now.second

        if time < 0:
            print('This player took more than 1 minute to made his move\n')
        else:
            print('This player took', time, 'seconds to made his move\n')


def main():
    named_players = validator()
    table=layout()
    count=1
    pp.pprint(table)
    last_player='O'
   
    while not report_winners(table) and not report_draw(table):
        if count %2==0:
            now = datetime.now()
            now.second
            last_player='X'
            player_movements=handle_players_movements('X',table)
            render_movement(table,'X',player_movements['X'])
            time_per_play(now)

        else:
            now = datetime.now()
            now.second
            last_player='O'
            player_movements=handle_players_movements('O',table)
            render_movement(table,'O',player_movements['O'])
            time_per_play(now)
           
        if player_movements:
            count+=1   

    if report_winners(table):
        print('___WINNER___')
        print('The Winner is ' + named_players[last_player])
        winsound.PlaySound("*",winsound.MB_ICONASTERISK)

main()
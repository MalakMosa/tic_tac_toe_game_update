list = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
c = 1
player=0
print('enter the sympol of player1:')
player1=input()
print('enter the sympol of player2:')
player2=input()
def game_board(list):
    print("\n", list[0], "\n", list[1], "\n", list[2], "\n")


def player_move(s):
    global list
    print('enter the location in range of 0 to 2 of the row')
    i = input()
    print('enter the location in range of 0 to 2 of the column')
    j = input()
    global player
    global player1
    player+=1
    if player%2==0:
     list[int(i)][int(j)] =player2
    else:
      list[int(i)][int(j)] = player1

def win_horizontal(list):
    x = 0
    global player
    if player%2==0:
        global player2
        s=player2
    else :
        global player1
        s=player1
    if list[0][1] == list[0][0] == list[0][2] and list[0][2] !='*':
        print('congratulation {}'.format(s))
        x = 1
    elif list[1][0] == list[1][1] == list[1][2]  and list[1][2] != '*':
        print('congratulation {}'.format(s))
        x = 1
    elif list[2][0] == list[2][1] ==list[2][2] and list[2][2] != '*':
        print('congratulation {}'.format(s))
        x = 1
    if x == 1:
        global c
        c = 0
def win_vertical(list):
    x = 0
    global player
    if player % 2 == 0:
        global player2
        s = player2
    else:
        global player1
        s = player1
    if list[0][0] == list[1][0] == list[2][0] and list[0][0] !='*':
        print('congratulation {}'.format(s))
        x = 1
    elif list[0][1] == list[1][1] == list[2][1]  and list[1][1] != '*':
        print('congratulation {}'.format(s))
        x = 1
    elif list[0][2] == list[1][2] ==list[2][2] and list[2][2] != '*':
        print('congratulation {}'.format(s))
        x = 1
    if x == 1:
        global c
        c = 0
def winx1(list):
    x = 0
    global player
    if player % 2 == 0:
        global player2
        s = player2
    else:
        global player1
        s = player1
    if list[0][2] == list[1][1] == list[2][0] and list[0][2] != '*':
        print('congratulation {}'.format(s))
        x = 1
    elif list[0][0] == list[1][1] == list[2][2] and list[1][1] != '*':
        print('congratulation {}'.format(s))
        x = 1
    if x == 1:
        global c
        c = 0
def tie (list):
    x=0
    if '*' not in list[0] and '*' not in list[1] and '*' not in list[2]:
        print('it is tie')
        x=1
    if x == 1:
        global c
        c = 0
while (c):
    game_board(list)
    player_move('x')
    game_board(list)
    win_horizontal(list)
    win_vertical(list)
    winx1(list)
    tie(list)


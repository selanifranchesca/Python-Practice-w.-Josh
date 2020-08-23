stop = False

while(not stop):

    player_one = input("Player One: Rock, Paper, or Scissors: ")
    player_two = input("Player Two: Rock, Paper, or Scissors: ")

    if player_one == player_two:
        print('DRAW GAME')
    elif player_one == 'Rock' and player_two == 'Paper':
        print('Player 2 Wins!')
    elif player_one == 'Rock' and player_two == 'Scissors':
        print('Player 1 Wins!')
    elif player_one == 'Paper' and player_two == 'Rock':
        print('Player 1 Wins!')
    elif player_one == 'Paper' and player_two == 'Scissors':
        print('Player 2 Wins!')
    elif player_one == 'Scissors' and player_two == 'Rock':
        print('Player 2 Wins!') 
    elif player_one == 'Scissors' and player_two == 'Paper':
        print ('Player 1 Wins!')
    else:
        print('Wrong answer, please type Rock, Paper, or Scissors in your next attempt.')

    checkpoint = input('Start a new game? Yes/No')
    if checkpoint == 'Yes':
        print('New Game Starting Soon')
    elif checkpoint == 'No':
        stop = True
        print('GAME OVER')
    else:
        print('Wrong answer. Please reply Yes or No.')

    

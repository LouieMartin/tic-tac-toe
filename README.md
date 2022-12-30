# Tic-Tac-Toe

Hello 👋, I built a Tic-Tac-Toe AI with the Negamax algorithm.
This AI can be transferred into other board games, but I just chose Tic-Tac-Toe
for simplicity.

## How-to-use

First you need to clone the project, like this:
```
git clone https://github.com/LouieMartin/tic-tac-toe.git tictactoe
```

Now you can implement the game outside the directory `tictactoe`, like this:
```py
from tictactoe import TicTacToe

# Initialize the board.
board = TicTacToe()

# Initialize the game loop.
while True:
    if board.game_over:
        if board.draw:
            print('It is a draw!')
            break
        
        print(f'{board.winner} won!')
        break
    
    try:
        # Get user input square.
        row, column = input(f'{board.winner} to move (e.g. 2,3): ').split(',')

        # Place square based on use input square
        board.put_piece((int(row) - 1, int(column) - 1))

        # Render the board to the terminal.
        board.render()
    except:
        print('Invalid input.')
```
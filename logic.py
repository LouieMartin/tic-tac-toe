from . import IllegalSquareError

PIECE_CHARACTER_MAP = {
    None: '.',
    'x': 'x',
    'o': 'o',
}

class TicTacToe:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.move_count = 0
        self.winner = None
        self.draw = False
        self.turn = 'x'
    
    def render(self):
        """
            Renders the tic-tac-toe board.
        """

        for row in self.board:
            for piece in row:
                print(PIECE_CHARACTER_MAP[piece], end='   ')
            print('\n')
    
    def get_legal_squares(self) -> list[tuple[int, int]]:
        """
            Gets all the legal squares the player can place.
        """

        if self.game_over:
            return []

        squares: list[tuple[int, int]] = []

        for row in range(3):
            for column in range(3):
                if self.board[row][column] is None:
                    squares.append((row, column))

        return squares

    def put_piece(self, square: tuple[int, int] | list[int, int]):
        """
            Places a piece on a specific square on the board.
        """

        row, column = square

        if self.board[row][column] is None:
            self.board[row][column] = self.turn
            self.move_count += 1

            # Check for columns.
            for index in range(3):
                if self.board[row][index] != self.turn:
                    break
                
                if index == 2:
                    self.winner = self.turn
                    self.game_over = True
                
            # Check for rows.
            for index in range(3):
                if self.board[index][column] != self.turn:
                    break
                
                if index == 2:
                    self.winner = self.turn
                    self.game_over = True
            
            # Check for diagonals.
            if column == row:
                for index in range(3):
                    if self.board[index][index] != self.turn:
                        break
                    
                    if index == 2:
                        self.winner = self.turn
                        self.game_over = True
            
            # Check for anti-diagonals.
            if column + row == 2:
                for index in range(3):
                    if self.board[index][2 - index] != self.turn:
                        break
                
                    if index == 2:
                        self.winner = self.turn
                        self.game_over = True
            
            # Checks for draws.
            if self.move_count == 9:
                self.game_over = True
                self.draw = True
            
            # Switch turns.
            if self.turn == 'x':
                self.turn = 'o'
            else:
                self.turn = 'x'

        else:
            # Raise an error if the square is invalid.
            raise IllegalSquareError()

class TicTacToe:
    def __init__(self):
        # Initialise the game board with empty spaces
        self.board = [' ' for _ in range(9)]

    def display_board(self):
        """Display the current state of the board."""
        print('Current Board')
        for i in range(3):
            print("  |  ".join(self.board[i * 3:(i + 1) * 3]))
            if i < 2:
                print("------------")
            print()

    def player_move(self):
        """Handle the player's move."""
        position = int(input("Enter your move (0-8): "))
        while self.board[position] == 'X' or self.board[position] == 'O':
            position = int(input("Enter your move (0-8): "))
        while position < 0 or position > 8:
            print('Invalid, try again')
            position = int(input("Enter your move (0-8): "))
        self.board[position] = 'X'

    def is_game_end(self, player):
        """Check if the game has ended either in a win or a draw."""
        if self.is_winner(player):
            self.display_board()
            print(f"{'You' if player == 'X' else 'I'} win!")
            return True
        elif self.is_draw():
            self.display_board()
            print("It's a draw!")
            return True
        return False

    def is_draw(self):
        """Check if the game is a draw."""
        # TODO: Return True if there are no empty spaces left
        return ' ' not in self.board

    def is_winner(self, player):
        """Check if the given player ("X" or "O") has won the game."""
        win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                        [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(self.board[i] == player for i in solution) for solution in win_conditions)

    def minimax(self, is_maximising, alpha, beta):
        """Minimax algorithm to evaluate the best move."""
        if self.is_winner('X'): return -1
        if self.is_winner('O'): return 1
        if '' not in self.board: return 0
        if is_maximising:
            best_score = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(False, alpha, beta)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:  # Prune the search tree
                        break
            return best_score
        else:  # Computer - ('O') is minimising
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(True, alpha, beta)
                    self.board[i] = ' '
                    best_score = max(score, best_score) #could be min
                    beta = min(beta, score)
                    if beta <= alpha:  # Prune the search tree
                        break
            return best_score

    def computer_move(self):
        """Make a move for the computer using the minimax algorithm."""
        # TODO: Use minimax to select the best move for the computer
        best_score = float('inf')  # The computer ('O') minimises
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(True, float('-inf'), float('inf'))
                self.board[i] = ' '
                if score < best_score:  # Minimising: look for the lowest score
                    best_score = score
                    best_move = i
        if best_move is not None:
            self.board[best_move] = 'O'
        pass

    def run(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while True:
            self.display_board()
            self.player_move()
            if self.is_game_end('X'): break
            self.computer_move()
            if self.is_game_end('O'): break

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
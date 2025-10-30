player, opponent = 'x', 'o'

def printBoard(board):
    print()
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            print(board[i][j], end=" ")
        print()
    print()

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False

def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return 10
            elif (b[row][0] == opponent):
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == player):
                return 10
            elif (b[0][col] == opponent):
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == player):
            return 10
        elif (b[0][0] == opponent):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent):
            return -10

    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)

    if (score == 10):
        return score

    if (score == -10):
        return score

    if (isMovesLeft(board) == False):
        return 0

    if (isMax):
        best = -1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'

                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

def checkWinner(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    if not isMovesLeft(board):
        return 'tie'
    return None

def playGame():
    # Initialize the board
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    
    print("Welcome to Tic Tac Toe!")
    print("You will be 'o' and the AI will be 'x'")
    print("Enter your move as row (0-2) and column (0-2)")
    print("For example: '1 2' for middle row, right column")
    
    while True:
        # AI's turn
        bestMove = findBestMove(board)
        board[bestMove[0]][bestMove[1]] = player
        print("\nAI's move:")
        printBoard(board)
        
        # Check if AI won
        winner = checkWinner(board)
        if winner:
            break
            
        # Player's turn
        while True:
            try:
                row, col = map(int, input("Enter your move (row col): ").split())
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '_':
                    break
                else:
                    print("Invalid move! Try again.")
            except:
                print("Invalid input! Please enter two numbers separated by space.")
        
        board[row][col] = opponent
        print("\nYour move:")
        printBoard(board)
        
        # Check if player won
        winner = checkWinner(board)
        if winner:
            break
    
    # Game over
    if winner == 'tie':
        print("It's a tie!")
    elif winner == player:
        print("AI wins!")
    else:
        print("You win!")

# Start the game
if __name__ == "__main__":
    while True:
        playGame()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")

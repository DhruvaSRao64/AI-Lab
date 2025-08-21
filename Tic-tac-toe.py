import math

def print_board(board):
	print()
	for i in range(3):
		print(" | ".join(board[i]))
		if i < 2:
			print("---------")
	print()

def check_winner(board):
	# Rows, columns and diagonals
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != ' ':
			return board[i][0]
		if board[0][i] == board[1][i] == board[2][i] != ' ':
			return board[0][i]
	if board[0][0] == board[1][1] == board[2][2] != ' ':
		return board[0][0]
	if board[0][2] == board[1][1] == board[2][0] != ' ':
		return board[0][2]
	return None

def is_full(board):
	return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
	winner = check_winner(board)
	if winner == 'O':
		return 1
	elif winner == 'X':
		return -1
	elif is_full(board):
		return 0

	if is_maximizing:
		best_score = -math.inf
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = 'O'
					score = minimax(board, depth + 1, False)
					board[i][j] = ' '
					best_score = max(score, best_score)
		return best_score
	else:
		best_score = math.inf
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = 'X'
					score = minimax(board, depth + 1, True)
					board[i][j] = ' '
					best_score = min(score, best_score)
		return best_score

def computer_move(board):
	best_score = -math.inf
	move = None
	for i in range(3):
		for j in range(3):
			if board[i][j] == ' ':
				board[i][j] = 'O'
				score = minimax(board, 0, False)
				board[i][j] = ' '
				if score > best_score:
					best_score = score
					move = (i, j)
	if move:
		board[move[0]][move[1]] = 'O'

def user_move(board):
	while True:
		try:
			pos = int(input("Enter your move (1-9): "))
			if pos < 1 or pos > 9:
				print("Invalid position. Choose 1-9.")
				continue
			row = (pos - 1) // 3
			col = (pos - 1) % 3
			if board[row][col] != ' ':
				print("Cell already taken. Choose another.")
				continue
			board[row][col] = 'X'
			break
		except ValueError:
			print("Please enter a valid number.")

def main():
	board = [[' ' for _ in range(3)] for _ in range(3)]
	print("Welcome to Tic Tac Toe!")
	print("You are X. Computer is O.")
	print("Positions are numbered 1-9 as follows:")
	print("1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n")
	while True:
		print_board(board)
		if check_winner(board) or is_full(board):
			break
		user_move(board)
		if check_winner(board) or is_full(board):
			break
		computer_move(board)

	print_board(board)
	winner = check_winner(board)
	if winner == 'X':
		print("Congratulations! You win!")
	elif winner == 'O':
		print("Computer wins! Better luck next time.")
	else:
		print("It's a draw!")

if __name__ == "__main__":
	main()

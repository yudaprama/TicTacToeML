# Main board where games are played

class Board(object):
	
	# Initializes board, move list of the game and number of moves played in the game
	def __init__(self):
		
		self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.playerToMove = 1
		self.movesPlayed = 0
		self.moveList = []
	
	# Displays all elements in the board
	def displayBoard(self):
		
		i = 0
		
		for elements in self.board:
			
			if (i is 2) or (i is 5) or (i is 8):
				print(elements)
			
			else:
				print(elements, end=" ")
			
			i = i + 1
	
	# Makes a move on the tic tac toe board
	def makeMove(self, squareNumber):
		
		if self.squareIsEmpty(squareNumber):
			
			self.board[squareNumber] = self.playerToMove
			self.movesPlayed = self.movesPlayed + 1
			self.moveList.append(squareNumber)
			
			if self.playerToMove is 1:
				self.playerToMove = 2
			else:
				self.playerToMove = 1
	
	# Checks if square is empty
	def squareIsEmpty(self, squareNumber):
		
		if self.board[squareNumber] is 0:
			return 1
		else:
			return 0
	
	# Resets all values to their default states
	def resetBoard(self):
		
		self.playerToMove = 1
		self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.movesPlayed = 0
		self.moveList.clear()
	
	# Checks the board for winning/losing or drawing conditions (returns 1 for win/loss and 2 for draw and 0 otherwise)
	def isWin(self):
		
		if (((self.board[0] == 1 and self.board[1] == 1 and self.board[2] == 1) or (
				self.board[3] == 1 and self.board[4] == 1 and self.board[5] == 1) or (
				     self.board[6] == 1 and self.board[7] == 1 and self.board[8] == 1) or (
				     self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1) or (
				     self.board[0] == 1 and self.board[3] == 1 and self.board[6] == 1) or (
				     self.board[1] == 1 and self.board[4] == 1 and self.board[7] == 1) or (
				     self.board[2] == 1 and self.board[5] == 1 and self.board[8] == 1) or (
				     self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1))
				or ((self.board[0] == 2 and self.board[1] == 2 and self.board[2] == 2) or (
						self.board[3] == 2 and self.board[4] == 2 and self.board[5] == 2) or (
						    self.board[6] == 2 and self.board[7] == 2 and self.board[8] == 2) or (
						    self.board[0] == 2 and self.board[4] == 2 and self.board[8] == 2) or (
						    self.board[0] == 2 and self.board[3] == 2 and self.board[6] == 2) or (
						    self.board[1] == 2 and self.board[4] == 2 and self.board[7] == 2) or (
						    self.board[2] == 2 and self.board[5] == 2 and self.board[8] == 2) or (
						    self.board[2] == 2 and self.board[4] == 2 and self.board[6] == 2))):
			
			return 1
		
		elif self.movesPlayed is 9:
			
			return 2
		
		else:
			
			return 0

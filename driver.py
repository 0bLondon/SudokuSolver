import time
from sudoku import Sudoku

ERROR = False
SOLVED = True

def backtracking(sudoku, assignment):
	if (len(assignment) == len(sudoku.variables)):
		return assignment

	var = select_unassigned_variable(sudoku, assignment)

	for value in order_domain_value(sudoku, var):
		if(sudoku.consistent(var, value, assignment)):
			sudoku.assign(var, value, assignment)
			result = backtracking(sudoku, assignment)

			if result:
				return result

			sudoku.unassign(var, assignment)

	return {}

def select_unassigned_variable(sudoku, assignment):
	unassigned_variables = []
	for var in sudoku.variables:
		if var not in assignment:
			unassigned_variables.append(var)

	return min(unassigned_variables, key=lambda var: len(sudoku.domains[var]))


def order_domain_value(sudoku, var):
	if len(sudoku.domains[var]) == 1:
		return sudoku.domains[var]

	return sorted(sudoku.domains[var], key = lambda val: num_conflicts(sudoku, var, val))



def num_conflicts(sudoku, var, val):

      n_conflicts = 0

      for neighbor in sudoku.neighbors[var]:
         if len(sudoku.domains[neighbor]) > 1 and val in sudoku.domains[neighbor]:
            n_conflicts += 1

      return n_conflicts


def solve_sudoku_ac3(sudoku):
	if not sudoku.solved():
		assignment = {}

		# Set initial values
		for var in sudoku.variables:
			if len(sudoku.domains[var]) == 1:
				assignment[var] = sudoku.domains[var][0]

		assignment = backtracking(sudoku, assignment)

		for domain in sudoku.domains:
			if len(domain) > 1 and (domain in assignment):	
				sudoku.domains[domain] = assignment[domain]

		if (not assignment):
			print("Error: There is no solution to this sudoku puzzle")
			return ERROR
		return SOLVED;

def print_init_board(board):
	string = ''
	count = 1
	for val in board:

		if (val =='0'):
			string = string + '-' + ' '
		else:
			string = string + val + ' '

		if(count % 9 == 0):
			string += '\n'
		elif(count % 3 == 0):
			string += '|'
		if(count % 27 == 0 and count != 81):
			string += '-------------------\n'
		count += 1
	print(string)


def print_solved_board(sudoku):
		string = ''
		count = 1
		for var in sudoku.variables:
			string = string + str(sudoku.domains[var]) + ' '
			if(count % 9 == 0):
				string += '\n'
			elif(count % 3 == 0):
				string += '|'
			if(count % 27 == 0 and count != 81):
				string += '-------------------\n'
			count += 1
		print(string)

def init_board():

	BOARDS = {
		# NO_SOLUTION
		1: "800000000003600000070090200050007000000045700000100030001000068008500010099999999",
		# EASY
		2: "608702100400010002025400000701080405080000070509060301000006750200090008006805203",
		# MEDIUM
		3: "000540008600002300007003090031050020000000000040030710090700200008600005100024000",
		# HARD
		4: "070042000000008610390000007000004009003000700500100000800000076054800000000610050",
		# EXTREMELY_HARD
		5: "800000000003600000070090200050007000000045700000100030001000068008500010090000400",
	}

	user_in = input("Would you like to use a preloaded Sudoku board?: (y/n)")
	if(user_in == "Y" or user_in == "y"):
		print("Choose one of the following levels:")
		print("[1] No Solution")
		print("[2] Easy")
		print("[3] Medium")
		print("[4] Hard")
		print("[5] Hardest in the World")
		user_in = input("Please input the level of difficulty: ")
		return BOARDS[int(user_in)]
	elif(user_in == "N" or user_in == "n"):
		user_in = input("Please input the puzzle in one line. Any blanks should be replaced with a 0.")
		return user_in
	else:
		print("Invalid input")
		return ""

if __name__== '__main__':

	board = init_board()
	if(not board):
		exit()

	print()
	print_init_board(board)
	sudoku = Sudoku(board)

	start_time = time.time()
	solved = solve_sudoku_ac3(sudoku)
	end_time = time.time()
	print()
	if(solved):
		print_solved_board(sudoku)
		print("Solve Time: " + str(end_time - start_time) + " seconds")
	
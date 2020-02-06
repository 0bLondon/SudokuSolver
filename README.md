## Sudoku Solver - CSP
### Ben London

Ran and tested on Python 3.7.1 using command:
	`~$ python3 driver.py`


driver.py contains an implementation of the AC-3 algorithm 
(Arc Consistency 3 algorithm) and sudoku.py contains an 
implementation of a Sudoku Board Class. The program primarily 
makes use of backtracking and forward checking. The algorithm 
solves any sudoku puzzle or determines if there is no solution
in about 0-2 seconds. 

The board can be inputted manually(not recommended) or the user 
can choose a board from a list of difficulty levels after running
the driver. If the board is inputted manually it must be of the 
following form: 
	- Any number should be inputted as the corresponding 
	  character in the range 1-9
	- Blank spaces must be represented as a 0
	- The entire board should be inputted as a long
	  81 character string
	- Examples of possible inputs are below
	
Preloaded Boards:

	NO_SOLUTION
	800000000003600000070090200050007000000045700000100030001000068008500010099999999
	
	EASY
	608702100400010002025400000701080405080000070509060301000006750200090008006805203
	
	MEDIUM
	000540008600002300007003090031050020000000000040030710090700200008600005100024000
	
	HARD
	070042000000008610390000007000004009003000700500100000800000076054800000000610050
	
	EXTREMELY_HARD
	800000000003600000070090200050007000000045700000100030001000068008500010090000400

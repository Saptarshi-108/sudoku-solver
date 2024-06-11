#we use backtracking algo to solve the problem every time an unsolved cell comes up.
from structure import Sudoku


def solve_algo(structure):

    row,col=structure.empty_cell()
    if row is None:
        return True # this means that if there is no empty space then the sudoku is solved.
      
    for num in range(1,10):
        if structure.valid_move(row,col,num): #checks for valid move.
            structure.place_num(row,col,num)  #places the value of a num as move is valid.
            if structure.solved(): #checks if sudoku is solved.
                return True
            
    return False #no valid number can be placed.
    
    
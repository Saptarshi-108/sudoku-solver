    # grid - structure of the sudoku board consisting of 2-D array
    #size - size of the 2-d array
class Sudoku:
    def __init__(self,grid): 
        self.grid=grid 
        self.size=size
        
    #tests whether or not column is present in grid.    
    def valid_col(self,col,num):
        return num not in [self.grid[row][col] for row in range(self.size)]
  
     #tests whether row is present in grid.   
    def valid_row(self,row,num):
        return num not in self.grid[row]
    
    # check whether change is possible or not.(change within grid)
    def valid_move(self,row,col,num):
        return(
            self.valid_col(col,num) and self.valid_row(row,num) and self.valid_box(row,col,num)
        )
    
    #checks the presence of valid box 
    def valid_box(self,row,col,num): 
        beg_row=3*(row//3)
        beg_col=3*(col//3)
        for i in range(beg_row,beg_row+3):
            for j in range(beg_col,beg_col+3):
                if self.grid[i][j]==num:
                    return False
        return True
    
    #outputs if the grid is correct.all the items in the loop traversed are true, then it is returned as true.
    #it goes through each cell for presence of a cel=num and if 0 returns false.
    def solved(self):
        return all(all(cell!=0 for cell in row )for row in self.grid)
    
    #traverses and finds the empty cells.
    def empty_cell(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col]==0:
                    return row,col
    #'line' stores rows of grids as strings.
    #'map' function converts each element in row to a string.
    # converts 2-d grids to a string representation.             
    def __str__(self):
        line=[]
        for row in self.grid:
            line.append(" ".join(map(str,row)))
        return "\n".join(line)
    
        
        
        
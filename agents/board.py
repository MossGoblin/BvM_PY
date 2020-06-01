import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import config as cc

class Board():
    
    grid = None
    

    def __init__(self):
        b_state = cc.BOARD_STATE
        l_defs = cc.LINE_DEFS


        board_chain = self.init_board()
        # create empty grid
        # use 1d for convenience ??
        '''
        rotating once 90 degrees counterclockwise => value + 2 mod 8

        for each configuration:
            check if in dictionary
            if not: up to 3 rotations until found in dictionary
        '''


    def init_board(self):
        # recursive
        # base case - nine pieces on the board
        # B starts first
        latest_piece = cc.EMPTY
        available_cells = self.get_available_cells()

        #HERE
        return False


    def check_line(self, line):
        # check if all cells in the line are of one type and not 0
        # return True if the line is a win, else return false
        if (self.b_state[self.l_defs[line[0]]] == 
            self.b_state[self.l_defs[line[1]]] == 
            self.b_state[self.l_defs[line[2]]]) & (self.b_state[self.l_defs[line[0]] != 0]):
            return True
        return False
    
    def check_all_lines(self):
        # check if any of the lines is a win
        # return True if so
        # else return False
        for line in range(9):
            if (self.check_line(line) == True):
                return True
        return False

    def get_available_cells(self):
        # returns all cells that are available for placement
        # skips cells that can produce win
        # TODO extend method to work with check_cell for only one of the agents
        availables = []
        for cell in self.b_state:
            if (cell != 0) & (self.check_cell(cell, 1) == False) & (self.check_cell(cell, 2) == False): # empty cell that can not produce a win
                availables.append(cell)
        return availables

    def check_cell(self, cell, agent):
        # check if placing a mark on a cell will produce a win line
        # return True if at least one line would be win with the agent value
        # return False is the agent value produces no wins
        # iterate through lines to find the ones that include that cell

        # check if the cell is available at all
        if self.b_state[cell] != 0:
            print(f'checked cell {cell} for win, but it is occupied')

        # build a triplet from the board state with the agent value in the cell in question
        for line in self.l_defs: # for each line
            if cell in line: # if the line has the cell in question
                counter = 0
                triplet = []
                for line_cell in line: # for each cell in the line
                    if line_cell == cell:
                        triplet[counter] = agent # place the agent value on the cell in question
                    else:
                        triplet[counter] = self.b_state[cell] # get the cell value from the board state
                    counter += 1
        
            # check the triplet for win
            if (triplet[0] == triplet[1] == triplet[2]) & (triplet[0] != 0):
                return True

        return False
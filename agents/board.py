import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import config
import random

class Board():
    def __init__(self):
        self.grid = None
        self.b_state = config.BOARD_STATE
        self.l_defs = config.LINE_DEFS
        self.board_chain = self.init_board()
        # create empty grid
        # use 1d for convenience ??
        '''
        rotating once 90 degrees counterclockwise => value + 2 mod 8

        for each configuration:
            check if in dictionary
            if not: up to 3 rotations until found in dictionary
        '''


    def init_board(self):
        available_cells = self.get_available_cells()
        check = 0
        # random selection check
        next_random_cell_index = random.randrange(len(available_cells))
        next_random_cell = available_cells[next_random_cell_index]

        # recursive
        # base case - nine pieces on the board
        # B starts first
        latest_piece = config.B_PIECE
        bracket = config.B_PIECE + config.M_PIECE
        # step:
        # get available cells
        # select and fill in a cell
        # alternate pices
        # check for base case
        for counter in range(10):
            available_cells = self.get_available_cells()
            next_random_cell_index = random.randrange(len(available_cells))
            next_random_cell = available_cells[next_random_cell_index]
            config.BOARD_STATE[next_random_cell_index] = latest_piece
            latest_piece = bracket - latest_piece

        check = 0




        #HERE
        return False


    def get_count(self, state):
        counter = 0
        for cell in state:
            if cell == 0:
                counter += 1
        return counter
    
    def check_line(self, line, state):
    # check if all cells in the line are of one type and not 0
    # return True if the line is a win, else return false
        cell_a = state[self.l_defs[line][0]]
        cell_b = state[self.l_defs[line][1]]
        cell_c = state[self.l_defs[line][2]]
        if (cell_a == 
            cell_b == 
            cell_c) & (cell_a != 0):
            return True
        return False
    
    def check_all_lines(self, state):
        # check if any of the lines is a win
        # return True if so
        # else return False
        for line in range(8):
            if (self.check_line(line, state) == True):
                return True
        return False

    def get_available_cells(self):
        # TODO extend method to work with check_cell for only one of the agents
        # returns all cells that are available for placement
        # skips cells that can produce win
        availables = []
        index = -1
        for cell in self.b_state: #
            index += 1
            if (cell == 0):
                cell_one = self.check_cell(index, 1)
                cell_two = self.check_cell(index, 2)
                if (cell_one == False) & (cell_two == False): # empty cell that can not produce a win
                    availables.append(index)
        return availables

    def check_cell(self, cell, agent):
        # check if placing a mark on a cell will produce a win line
        # return True if at least one line would be win with the agent value
        # return False is the agent value produces no wins
        # iterate through lines to find the ones that include that cell

        # check if the cell is available at all
        if self.b_state[cell] != 0:
            print(f'checked cell {cell} for win, but it is occupied')
            raise

        # TODO change logic:
        # add the agent mark
        # then check all lines

        # fill in the cell
        check_state = config.BOARD_STATE.copy()
        check_state[cell] = agent
        # check for any win lines
        result = self.check_all_lines(check_state)
        return result

        # # build a triplet from the board state with the agent value in the cell in question
        # for line in self.l_defs: # for each line
        #     if cell in line: # if the line has the cell in question
        #         counter = 0
        #         triplet = []
        #         for line_cell in line: # for each cell in the line
        #             if line_cell == cell:
        #                 triplet.append(agent) # place the agent value on the cell in question
        #             else:
        #                 triplet.append(self.b_state[cell]) # get the cell value from the board state
        #             counter += 1
        
        #         # check the triplet for win
        #         if (triplet[0] == triplet[1] == triplet[2]) & (triplet[0] != 0):
        #             return True # WTF - need to get out of the method

        # return False
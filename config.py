# game logs
GAME_LOG_FILE_NAME = ''
GAME_LOG_SUBDIR = 'gamelogs/'
GAME_LOG_SUBDIR_DATE = False

# agents
B_PIECE = 1
M_PIECE = 2
EMPTY = 0

# board
LINE_DEFS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

POSITION_MAP = [0, 2, 3, 4, 5, 6, 7, 8]
        # 0 1 2
        # 3 4 5
        # 6 7 8

ROTATION_MAP = [2, 1, 8, 3, 0, 7, 4, 5, 6] # will not be used
        # 2 1 8
        # 3 0 7
        # 4 5 6

BOARD_STATE = [0, 0, 0, 0, 0, 0, 0, 0, 0]

STATES_MAP = []
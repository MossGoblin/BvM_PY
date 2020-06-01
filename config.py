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
    [1, 8, 7],
    [2, 0, 6],
    [3, 4, 5],
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
    [1, 0, 5],
    [3, 0, 7]
]

POSITION_MAP = [0, 2, 3, 4, 5, 6, 7, 8]
        # 0 1 2
        # 3 4 5
        # 6 7 8

ROTATION_MAP = [2, 1, 8, 3, 0, 7, 4, 5, 6]
        # 2 1 8
        # 3 0 7
        # 4 5 6

BOARD_STATE = [1, 1, 0, 0, 0, 0, 0, 0, 0]
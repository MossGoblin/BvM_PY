#!/usr/bin/env python3
from datetime import datetime, timedelta

# locals
import config
from agents import board
from utils import secretariat

secretary = secretariat.Secretary()
brd = board.Board()

def main():
    secretary.jot(f'\nMAIN:: {str(datetime.now())}', 't')

if __name__ == '__main__':
    main()
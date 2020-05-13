#!/usr/bin/env python3
from datetime import datetime, timedelta
import config

#locals
#from agents import beast, menace, board
from utils import secretariat

secretary = secretariat.Secretary()

def main():
    secretary.jot(f'\nMAIN:: {str(datetime.now())}', 't')

if __name__ == '__main__':
    main()
import logging
from datetime import datetime, timedelta

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
logging.basicConfig(level=logging.INFO, handlers=[handler])
logging.getLogger('bvm').setLevel('INFO')

logger = logging.getLogger(__name__)

class Secretary:

    def __init__(self):
        # init file service for the secretary
        return

    def jot(self, notice, location='t'):
        if (location=='t'):
            logger.info(notice)
        elif (location=='f'):
            logger.info('\nSECR:: No file service has been established yet')
        else:
            logger.info('\nSECR:: specify target for message "f{notice} - either terminal (t) or file (f)')

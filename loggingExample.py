#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      maic
#
# Created:     25/01/2012
# Copyright:   (c) maic 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import logging
import os

logDir = os.path.dirname(__file__)+'/logs'
logger = logging.getLogger('loggingExample')
logger.setLevel(logging.DEBUG)
hdlr = logging.FileHandler(logDir+'/error.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

def main():
    logger.info("This is some information")
    logger.error("This is an error")

if __name__ == '__main__':
    main()

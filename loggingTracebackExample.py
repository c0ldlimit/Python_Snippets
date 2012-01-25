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

import traceback
import os
import datetime

def main():
    print 1/0

if __name__ == '__main__':
    try:
        main()
    except:
        fileDate = datetime.date.today().strftime("%Y%m%d")
        curDir = 'C:\\Temp'
        logFile = open(curDir+"\\"+fileDate+"_error.log","wb")
        traceback.print_exc(file=logFile)
        logFile.close()
        raise

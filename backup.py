#!/usr/bin/python3

# Imports
import sys
import pathlib
import shutil
from datetime import datetime
from backupcfg import jobs

# Variables

dstDir = "/home/ec2-user/environment/backups/"
timeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")

# Functions

# Main

if len(sys.argv) < 2:
    print("usage: python backup.py <job>\n")
    
else:
    job = sys.argv[1]
    
    print(job)
    
    if not job in jobs:
        print("error: invalid job-%s" % job)
    
    else:
        srcLoc = jobs[job]
        srcPath = pathlib.PurePath(srcLoc)
        print(srcLoc)
        
        dstLoc = dstDir + srcPath.name + "-" + timeStamp
        print(dstLoc)
        
    
        if pathlib.Path(srcLoc).is_dir():
            try:
                shutil.copytree(srcLoc, dstLoc)
            except:
                print("error: " + job + " FAIL")
        else:
            try:
                shutil.copy2(srcLoc, dstLoc)
            except:
                print("error: " + job + " FAIL")
 
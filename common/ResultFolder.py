#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def GetRunDirectory():
    
    allRunFolders = [fd for fd in os.listdir(".") if os.path.isdir(fd) and fd.startswith("TestRun")]
    latestFolder = max(allRunFolders,key=os.path.getmtime)
    return latestFolder
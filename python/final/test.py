#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import time
 
def test():
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime)
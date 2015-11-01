#!/usr/bin/env python  
       
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  12 14:48:27 2015

@author: Wenliang Zhao

mapper function for word count
"""

import sys  
       
# input comes from STDIN (standard input)  
for line in sys.stdin:  
    line = line.strip()  
    words = line.split()  
    for word in words:  
        print '%s\\t%s' % (word, 1)  

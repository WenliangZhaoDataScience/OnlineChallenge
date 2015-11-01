#!/usr/bin/env python  
   
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  12 14:48:27 2015

@author: Wenliang Zhao

reducer function for word count
"""

from operator import itemgetter  
import sys  
  
word2count = {}  
   
# input comes from STDIN  
for line in sys.stdin:  
    line = line.strip()  
   
    word, count = line.split('\\t', 1)  
    try:  
        count = int(count)  
        word2count[word] = word2count.get(word, 0) + count  
    except ValueError:  
        # count was not a number, so silently  
        # ignore/discard this line  
        pass  
  
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))  
  
for word, count in sorted_word2count:  
    print '%s%s'% ('{:<50}'.format(word), count)

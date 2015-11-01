#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  12 14:48:27 2015

@author: Wenliang Zhao

Program that calculates the median number of unique words per tweet.

Considering each update, median only shifts 0.5 position. This code remembers the last position of median. The time complexity is thus roughly O(1) (a bit increase when there is big gap between values, see lines 66 and 83)  
"""

import sys, os

def main(argv):
    if len(argv) != 3:
        print "3 args required!"
        print "Usage median_unique.py input.txt output.txt"
        exit(1)

    N_max = 10000
    input_file = sys.argv[1].strip()
    output_file = sys.argv[2].strip()
    count_array = [0] * N_max 
    median = 0                                                   ### current median value
    median_list = [0, 0]                                         ### 2 number list for median, if first number is 0, median is single number;  otherwise median is average of these two number
    internal_index = 0                                           ### for multiple number with same value, a index indicating current position of median within these numbers
    N_tw = 0                                                     ### number of valid tweets

    OUT = open(output_file, 'w')
    with open(input_file) as IN:
        for line in IN:
            line = line.strip()
            new_number = len(list(set(line.split())))
            if new_number > N_max or new_number <= 0:            ### assume the largest length within 9999 which is enough
                print "Error!!! length of word " + str(new_number) + " out of range!"
                exit(1)
        
            N_tw += 1
            count_array[new_number] += 1

            if median == 0:                                      ### initial case 
                median = new_number
                median_list = [0, new_number]

            elif N_tw % 2 == 1:                                  ### odd case
                OUT.write('\n')
                if new_number > median:                          ### new number larger than previous median, new median shifts 0.5 to the right
                    median = min(median_list[1], new_number)
                    if median_list[0] == median_list[1]:
                        internal_index += 0.5
                    else:
                        internal_index = 0
                        median_list = [0, median_list[1]]

                elif new_number == median:                      ### convention that new number equals to previous median is the same case as above (larger)
                    if median_list[0] == median_list[1]:
                        median = median_list[1]
                        internal_index += 0.5
                    else:
                        median = new_number
                        median_list = [median_list[0], median]
                        internal_index = 0

                else:                                          ### new number less than previous median, new median shifts 0.5 to the left
                    median = max(median_list[0], new_number)
                    if median_list[0] == median_list[1]:
                        internal_index -= 0.5
                    else:
                        internal_index = count_array[median] - 1
                        median_list = [0, median_list[0]]

            elif N_tw % 2 == 0:                                ### even case
                OUT.write('\n')
                if new_number > median:
                    if internal_index == count_array[median] - 1:
                        temp_index = median + 1
                        while(count_array[temp_index] == 0):
                            temp_index += 1
                        median_list = [median_list[1], temp_index]
                        median = (median_list[0] + median_list[1]) / 2.
                        internal_index = -0.5

                    elif internal_index < count_array[median] - 1:
                        median_list = [median, median]
                        internal_index += 0.5

                elif new_number == median:
                    internal_index += 0.5
                    median_list = [median, median]

                else:
                    if internal_index == 0:
                        temp_index = median - 1
                        while(count_array[temp_index] == 0):
                            temp_index -= 1
                        median_list = [temp_index, median]
                        median = (median_list[0] + median_list[1]) / 2.
                        internal_index = count_array[temp_index] - 1

                    else:
                        median_list = [median, median]
                        internal_index -= 0.5
            OUT.write("%.1f" % median)

    IN.close()
    OUT.close()

if __name__ == '__main__':
    main(sys.argv[:])

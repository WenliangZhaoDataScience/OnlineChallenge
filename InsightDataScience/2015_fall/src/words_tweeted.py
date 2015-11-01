#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  12 14:48:27 2015

@author: Wenliang Zhao

Program that calculates the total number of times each word has been tweeted.

Code using hadoop and map-reduce to count for words, mapper: count_mapper.py; reducer: count_reducer.py
"""

import sys, os, subprocess, glob

def main(argv):
    if len(argv) != 3:
        print "3 args required!"
        print "Usage word_tweets.py input.txt output.txt"
        exit(1)

    current_dir = os.getcwd()
    input_file = sys.argv[1].strip()
    output_file = sys.argv[2].strip()
    result_dir = current_dir + '/count_result'
    hadoop_home = os.getenv('HADOOP_HOME').strip()
    stream_jar = glob.glob(hadoop_home + '/contrib//streaming/hadoop-streaming*.jar')[0]
    mapper_file = current_dir + '/src/count_mapper.py'
    reducer_file = current_dir + '/src/count_reducer.py'

    call_str = 'hadoop jar ' + stream_jar + ' -mapper ' + mapper_file + ' -reducer ' + reducer_file + ' -file ' + mapper_file + ' -file ' + reducer_file + ' -input ' + input_file + ' -output ' + result_dir + ' -mapper cat -reducer aggregate'
 
    call_list = ['hadoop', 'jar', stream_jar, '-mapper', mapper_file, '-reducer', reducer_file, '-file', mapper_file, '-file', reducer_file, '-input', input_file, '-output', result_dir, '-mapper', 'cat', '-reducer', 'aggregate']

    print call_str
    subprocess.Popen(call_list).wait()

    if os.path.isfile(result_dir+"/_SUCCESS") == True:
        print "Code finished successfully!"
        result_file = glob.glob(result_dir+"/part*")[0]
        call_str = "mv " + result_file + " " + output_file
        print call_str
        os.system(call_str)
        call_str = "rm -rf " + result_dir
        print call_str
        os.system(call_str)

    else:
        print "Error occurs in map reduce!"
        exit(1)

if __name__ == '__main__':
    main(sys.argv[:])

       

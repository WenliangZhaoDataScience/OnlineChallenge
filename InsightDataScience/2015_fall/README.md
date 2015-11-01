Environment and libraries:
OSX 10.9.2
python 2.7
hadoop 1.2.1

Description of algorithms:

1. word count: did not consider writing data structure from scratch because hadoop already has the ability and works fine. Since the later work will anyway use distributed systems, choose not to make the code too complicated.
 
2. median update: GENERAL IDEA: for each update, median only shift 0.5 in position (this algorithm spends ~O(1) time for each update). DETAILS: list "count_array" stores the counts for each value; variable "median" stores the current median value; list "median_list" stores upper and lower values of median, if number of tweets is odd, the first values is 0, and the second value is median. If number of tweets is even, median equals the average of the two values; variable "internal_index" stores the relative position with in numbers having same value. E.g. if there are only 2 tweets with same length of 17. The index equals to 0.5, representing between 0 and 1.This index is used to help the position shifting for each update.


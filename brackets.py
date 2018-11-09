#!/bin/python3

import math
import os
import random
import re
import sys



YES = 'YES'
NO = 'NO'
BRACKETS = ['[', '{', '(', ')', '}', ']']
OPENBRACKETS = ['[', '{', '(']
CLOSEBRACKETS = [')', '}', ']']
CLOSE_TO_OPEN = {')':'(', '}':'{', ']':'['}

# Complete the braces function below.
def braces(values):
    '''
    (list(str)) -> list(str)
    This function takes a list of lines of text, and checks to see if they do
    or not, returning a string.
    '''
    ret_array = []
    # Go through every string
    for line in values:
        # Base case: No brackets or empty string
        if any(bracket in line for bracket in BRACKETS):
            ret_array.append(YES)
        # Second Base case: Odd length string (not matching brackets, ofc)
        elif (len(line) % 2 == 1):
            ret_array.append(NO)
        else:
            found_end = False
            # Need a var to hold index of the current symbol
            index = 0
            # We will have a Stack like checker (with no order), that is a list
            # which keeps track of how many of what we have
            push_pop = []
            # Loop formula until we find the root
            while (found_end is False):
                # if we just encountered an open bracket, increment var by 1
                if line[index] in OPENBRACKETS:
                    push_pop.append(line[index])
                # do the same as above for our closed brackets
                if line[index] in CLOSEBRACKETS:
                    # Try removing the hanging open from 'stack '(found a pair)
                    try:
                        push_pop.remove(CLOSE_TO_OPEN[line[index]])
                    # Otherwise, there are clearly more close brackets than open
                    except:
                        # Therefore, this string is invalid
                        ret_array.append(NO)
                        break;
                # increment the index, move onto next letter/symbol in formula
                index += 1
                # Now, it is time to check if everything is balanced
                if ((push_pop == []) and (index == len(line))):
                    ret_array.append(YES)
                elif index == len(line):
                    # Note: invalid case, escape the loop + give no! answer
                    found_end = True
                    ret_array.append(NO)
    return ret_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    values_count = int(input())
    values = []
    for _ in range(values_count):
        values_item = input()
        values.append(values_item)
    res = braces(values)
    fptr.write('\n'.join(res))
    fptr.write('\n')
    fptr.close()
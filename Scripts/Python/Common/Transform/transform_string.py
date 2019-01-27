import os
import sys

def roman_to_integer(in_str):
    '''
    Purpose : Convert input roman number (string) to integer equivalent.
    Input   : str
    Return  : int
    Example : f('XXXIX')=39; f('XXX'):30; f('CVII')=107; f('XCIX')=99
    '''
    substract = 0
    out_num = 0
    dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in range(0, len(in_str)):
        if i == len(in_str)-1:
            out_num += dictionary[in_str[i]] - substract
            substract = 0
        elif dictionary[in_str[i]] < dictionary[in_str[i+1]]:
            substract = dictionary[in_str[i]]
        elif dictionary[in_str[i]] >= dictionary [in_str[i]]:
            out_num += dictionary[in_str[i]] - substract
            substract = 0
        i+=1
    return out_num

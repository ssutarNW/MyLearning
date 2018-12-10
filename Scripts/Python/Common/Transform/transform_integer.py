import os
import sys

def reverse_integer(in_num):
    '''
    Purpose : Given a 32-bit signed integer, reverse digits of an integer.
              Assume that your function returns 0 when the reversed integer overflows.
    Input   : int
    Return  : int
    Example : f(123)=321; f(120)=21; f(-123)=-321;
    '''
    out_num=0
    tmp_num = in_num * -1 if in_num < 0 else in_num

    while tmp_num != 0:
        out_num = (out_num * 10) + (tmp_num % 10)
        tmp_num = tmp_num // 10

    if in_num < 0:
        out_num = out_num * -1

    if out_num == 0 or out_num > 2**31-1 or out_num < -2**31:
        return 0
    else:
        return out_num

def integer_to_roman(in_num):
    '''
    Purpose : Convert input integer number into roman equivalent.
    Input   : int
    Return  : str
    Example : f(39)=XXXIX; f(30):XXX; f(107)=CVII; f(99)=XCIX
    '''
    dictionary = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

    numerator = in_num
    denominator = 1000
    out_str=""

    while (numerator != 0):
        quotient = numerator // denominator
        if quotient != 0 :
            if quotient in range(1,4):
                out_str = out_str + (dictionary[denominator] * quotient)
            elif quotient == 4:
                out_str = out_str + (dictionary[denominator]) + dictionary[denominator*5]
            elif quotient == 5:
                out_str = out_str + dictionary[denominator*5]
            elif quotient in range(6,9):
                out_str = out_str + dictionary[denominator*5] + (dictionary[denominator] * (quotient - 5))
            elif quotient == 9:
                out_str = out_str + dictionary[denominator] + dictionary[denominator*10]
        numerator = numerator % denominator
        denominator = denominator // 10
        if denominator == 0: denominator = 1
    return out_str

if __name__ == "__main__":
    print ("reverse_integer({}) = {}".format(sys.argv[1], reverse_integer(int(sys.argv[1]))))
    print ("integer_to_roman({}) = {}".format(sys.argv[2], integer_to_roman(int(sys.argv[2]))))

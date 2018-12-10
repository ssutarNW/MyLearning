import os
import sys

def reverse_integer(in_num):
    '''
    Purpose : Given a 32-bit signed integer, reverse digits of an integer.
              Assume that your function returns 0 when the reversed integer overflows.
    Input   : Integer
    Return  : Integer
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

if __name__ == "__main__":
    print ("reverse_integer({}) = {}".format(sys.argv[1], reverse_integer(int(sys.argv[1]))))

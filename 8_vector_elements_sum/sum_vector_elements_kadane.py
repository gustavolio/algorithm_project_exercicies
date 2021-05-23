__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import sys
import numpy

#______________Input_Matrix______________#
matrix = []

input_string = sys.stdin.read()

input_string = input_string.split("\n")
input_string = input_string[:-1]

for line in input_string:
    new_line = []
    for num in line.strip().split(' '):
        new_line.append(num)

    matrix.append(new_line)


#input data iterator
reading_line = 0
#output string
output = ""

def type_cast_string_int(list):

    new = []
    for value in list:
        new.append(int(value))

    return new

#________Vector_Element_Sum________#

def bigger_sum(vector):

    max = vector[0]
    total = 0

    for value in vector:
        total += value

        if max < total:
            max = total

        if total < 0:
            total = 0

    return max

#__________Read_And_Run_Test_Cases__________#

n_test_cases = int(matrix[reading_line][0])
reading_line += 1

for test_case in range(n_test_cases):

    reading_line += 1

    vector = type_cast_string_int(matrix[reading_line])
    reading_line += 1

    result_sum = bigger_sum(vector)

    print("Soma maxima = {}".format(result_sum))
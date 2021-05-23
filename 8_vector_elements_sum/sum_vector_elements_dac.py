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
        new_line.append(int(num))

    matrix.append(new_line)


#input data iterator
reading_line = 0
#output string
output = ""

print(matrix)

#________Vector_Element_Sum________#

def bigger_sum(vector):

    if len(vector) < 3:
        return numpy.sum(vector)

    actual_sum = numpy.sum(vector)

    sum_1 = bigger_sum(vector[1:])
    sum_2 = bigger_sum(vector[:-1])

    old_sum = sum_1
    if old_sum < sum_2:
        old_sum = sum_2

    if actual_sum < old_sum:
        return old_sum
    return actual_sum

#__________Read_And_Run_Test_Cases__________#

n_test_cases = matrix[reading_line][0]
reading_line += 1

for test_case in range(n_test_cases):

    reading_line += 1

    vector = matrix[reading_line]
    reading_line += 1

    result_sum = bigger_sum(vector)

    print("Soma maxima = {}".format(result_sum))
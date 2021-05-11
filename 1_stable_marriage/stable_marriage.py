__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"
__status__ = "Test"

import numpy as np
import sys

matrix = []

input_string = sys.stdin.read()

input_string = input_string.split("\n")
input_string = input_string[:-1]

for line in input_string:
    new_line = []
    for num in line.split(' '):
        new_line.append(int(num))

    matrix.append(new_line)

#input data iterator
reading_line = 0

def stable_married(m, w):

    #column 0 -> man & 1 -> woman 
    status = [[0 for i in range(len(m))] for j in range(2)]
    #list of numbers of man's womans lists already proposed to
    propose = [0] * len(m)

    while 0 in status[0]:
        #select a free man
        free_man = status[0].index(0)

        woman = m[free_man][propose[free_man]] - 1
        propose[free_man] += 1 

        #check if woman is free
        if status[1][woman] == 0:
            status[1][woman] = free_man + 1
            status[0][free_man] = woman + 1
        else:
            fiance = status[1][woman]

            index_fiance = w[woman].index(fiance)
            index_man = w[woman].index(free_man)


            # Change the marriege based on the woman's preferences 
            if(index_man < index_fiance):
                status[1][woman] = free_man + 1
                status[0][free_man] = woman + 1

                status[index_fiance] = 0

    return status

        
def fill_output(m):
    string = ""

    for index,woman in enumerate(m[0]):
        man = index + 1
        string += "{} {}\n".format(man,woman)

    return string  


num_case_test = matrix[reading_line][0]
reading_line += 1
output = ""

i = 0
while i < num_case_test:

    #read number of marrieges
    num_marrieges = matrix[reading_line][0]
    reading_line += 1

    #create woman matrix
    w = [] 
    for num in range(num_marrieges):
        w.append(matrix[reading_line][1:])
        reading_line += 1

    #create man matrix
    m = [] 
    for num in range(num_marrieges):
        m.append(matrix[reading_line][1:])
        reading_line += 1

    stb_marrieges = stable_married(m,w)
    output += fill_output(stb_marrieges)    

    i += 1

output = output[:-1]
print(output)
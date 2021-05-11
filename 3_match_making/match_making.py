__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

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

#output string
output = ""

def get_maches(bach, spin):

    bach.sort(reverse=True)
    spin.sort(reverse=True)

    i = abs(len(bach) - len(spin))

    if i == 0:
        i = len(bach)

    bach = bach[i:]
    spin = spin[i:]

    if len(bach) != 0:
        return "{} {}".format(i,min(bach)[0])
    
    return "0"

n_cases = 0
while matrix[reading_line] != [0,0]:
    n_cases += 1

    #read num of bachelors and spinsters
    n_bach = matrix[reading_line][0]
    n_spin = matrix[reading_line][1]
    reading_line += 1

    #read bachelors and spinsters age
    bach_age = matrix[reading_line: (reading_line + n_bach)] 
    reading_line += n_bach

    spin_age = matrix[reading_line: (reading_line + n_spin)]
    reading_line += n_spin

    # print("Bach age: {}\nSpin age: {}\n".format(bach_age, spin_age))
    # exit()

    output += "Case {}: {}".format(n_cases, get_maches(bach_age, spin_age) + "\n")
    

output = output[:-1]
print(output)
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

#load balancing for bus drivers problem
def get_tax_day(n_drivers, limit, tax, routes):

    #sort in ascending order morning routes
    routes[0].sort()
    #sort in decending order afternoon routes
    routes[1].sort(reverse=True)

    extra_hours = []
    #sum values of morning and afternoon with the same index
    for index in range(len(routes[0])):
        result = routes[0][index] + routes[1][index]
        extra_hours.append(result - limit)

    #calculate extra hours
    total_extra_hours = 0
    for value in extra_hours:
        if value > 0:
            total_extra_hours += value

    #return tax value
    return str(total_extra_hours * tax)

output = ""
while(matrix[reading_line] != [0,0,0]):

    #read test case header
    bus_drivers = matrix[reading_line][0]
    drivers_limit = matrix[reading_line][1]
    tax_per_hour = matrix[reading_line][2]
    reading_line += 1

    #read routes
    routes = []
    for num in range(2):
        routes.append(matrix[reading_line])
        reading_line += 1

    output += get_tax_day(bus_drivers, drivers_limit, tax_per_hour, routes) + "\n"

output = output[:-1]
print(output)
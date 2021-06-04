__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import sys
import math

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

#________Closest_Points________#

# Euclidea distance between two cartesian points
def euclidean_dist(p1, p2):
    total = 0
    for i in range(2):
        total += (p1[i] - p2[i])**2

    return abs(math.sqrt(total))

# Mask to order vector by y coordinate
def take_y(elem):
    return elem[1]

# Creates vector that represents central zone, based on divisor line and sigma 
def create_s(sigma, l, vector):
    x_min = l - sigma
    x_max = l + sigma
    s = []

    # Select only points on central zone
    for point in vector:
        if x_min < point[0] and point[0] < x_max:
            s.append(point)
    
    # Sort vector based on y coordinate
    s.sort(key=take_y)
    return s


# Calculates min distance on central zone
def closest_pair_central(s):
    min_dist = math.inf
                
    for index, point in enumerate(s):
        #Only from the first 15 elements
        for i in range(1,8):
            if ((index+i) >= (len(s[index:])-1)):
                break 

            dist = euclidean_dist(point, s[index+i])

            if dist < min_dist:
                min_dist = dist
    
    return min_dist      

def closest_pair_central2(s, sig):
    min_dist = sig                    # comeco com a menor distancia encontrada...
               
    for index, point in enumerate(s):
        # print(index)
        # print(point)
        j = index+1
        while j < len(s) and (s[j][1] - s[index][1]) < min_dist:
            dist = euclidean_dist(s[index], s[j])
            if (dist <  min_dist):
                min_dist = dist
            j = j+1

    return min_dist      

def closest_pair_rec(vector, point, dist_min):
    if point > len(vector)-2:
        return dist_min
    
    dist = euclidean_dist(vector[point], vector[point+1])

    if dist < dist_min:
        dist_min = dist
    
    #Call the next point on vector
    return closest_pair_rec(vector, point+1, dist_min)


def closest_pair(vector):
    if len(vector) == 1:
        return "INFINITY"

    divisor = int(len(vector)/2)

    q = vector[:divisor] # Left side points
    r = vector[divisor:] # Right side points

    # print(q, "\n\n", r)

    sig_q = closest_pair_rec(q, 0, math.inf) # Min distance from left side
    sig_r = closest_pair_rec(r, 0, math.inf) # Min distance from right side
    sig = min(sig_q, sig_r) # Min distance between left side and right side

    print(sig_r, sig_q)

    l = int((q[-1][0] + r[0][0])/2) # Horizontal line that separate sides
    s = create_s(sig, l, vector) # Central zone points vector
    print(print(len(vector)), "  ---  ",len(s))
    d = closest_pair_central(s)
    # d = closest_pair_central2(s, sig)
    # d = closest_pair_rec(s, 0, sig) # Min distance from central zone

    print(sig_r, sig_q, d)
    
    # Return min distance
    result = min(sig, d)

    if result > 10000:
        return "INFINITY"
    return "%.4f" % result

#__________Read_And_Run_Test_Cases__________#
final = [0]
while(matrix[reading_line] != final):

    num_points = matrix[reading_line][0]
    reading_line += 1

    points_matrix = matrix[reading_line:reading_line+num_points]
    reading_line += num_points

    #Sort vector based on x coordinate
    points_matrix.sort()

    print(closest_pair(points_matrix), "\n")
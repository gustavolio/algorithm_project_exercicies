__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import sys

#______________Input_Matrix______________#
matrix = []

input_string = sys.stdin.read()

input_string = input_string.split("\n")
input_string = input_string[:-1]

for line in input_string:
    new_line = []
    for num in line.strip().split(' '):
        if num.isdigit():
            new_line.append(int(num))

    matrix.append(new_line)


#input data iterator
reading_line = 0
#output string
output = ""


#________Sultains_8_Queens_Problem________#


n_max = 8 #Num of rows and lines
lines = [0] * n_max #Queens positions, index == col, values = line
max_sum = 0 #Sum of values from queens positions
chess_board = [] #Value of chess board positions

#Check if the position is valid
def check(lin, col):
    for rp in range(col):
        # Check if exist another queen in the same line and the same diagonal
        if(lines[rp] == lin or (abs(lines[rp]-lin) == abs(rp-col))):
            return False
    return True

def backtraking(c, way_sum):
    #When 8 queens are positioned
    if c == n_max:
        global max_sum
        #Change the max_sum if actual arrangement is biggest
        if(way_sum > max_sum):
            max_sum = way_sum
    else:
        for lin in range(n_max):
            if check(lin, c):
                lines[c] = lin
                way_sum += chess_board[lin][c]
                backtraking(c+1, way_sum)
                way_sum -= chess_board[lin][c]



#__________Read_And_Run_Test_Cases__________#

n_test_cases = matrix[reading_line][0]
reading_line += 1

for test_case in range(n_test_cases):

    chess_board = matrix[reading_line:reading_line+8] #change 8 per n_max variable
    reading_line += 8

    # print("Este é o tabuleiro {}\nTamanho: {}".format(chess_board, len(chess_board)))

    max_sum = 0
    backtraking(0,0)

    output += "{}".format(max_sum).rjust(5) + "\n"

output = output[:-1]
print(output)

    

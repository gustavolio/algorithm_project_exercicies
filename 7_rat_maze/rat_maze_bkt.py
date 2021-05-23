__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021" #last update: 11 mai
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import sys
import itertools

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
moves = [[1,0],
         [0,1],
         [-1,0],
         [0,-1]]

class Coordinate:
     def __init__(self, x, y):
         self.x = x
         self.y = y

def print_sol(sol):
    for line in sol:
        string = ' '.join([str(item) for item in line])
        print(string)


def finish(coord, maze):
    if coord.x == len(maze)-1 and coord.y == len(maze)-1 and maze[coord.x][coord.y] == 1:
        return True
    return False

def get_next_moves(coord, maze, sol):
    new_moves = []
    maze_size = len(maze)

    for mov in moves:
        next_coord = Coordinate(coord.x + mov[0], coord.y + mov[1])
        #Check if next_coord is inside of maze bounds
        if next_coord.x < maze_size and next_coord.x >= 0 and next_coord.y < maze_size and next_coord.y >= 0:
            #Check if next_coord isn't obstacle or isn't visited
            if maze[next_coord.x][next_coord.y] == 1 and sol[next_coord.x][next_coord.y] == 0:
                new_moves.append(next_coord)
    
    return new_moves


counter_states = itertools.count()
def find_way(coord, maze, sol):
    next(counter_states)

    if(finish(coord, maze)):
        print("Steps: {}".format(counter_states))
        return True

    for mov in get_next_moves(coord, maze, sol):
            sol[mov.x][mov.y] = 1

            if(find_way(mov, maze, sol)):
                return True

            sol[mov.x][mov.y] = 0

    return False


#________Rat_in_a_Maze_Problem________#

n_test_cases = matrix[reading_line][0]
reading_line += 1

for test_case in range(n_test_cases):

    maze_shape = matrix[reading_line][0]
    reading_line += 1

    maze = matrix[reading_line:reading_line+maze_shape]
    reading_line += maze_shape

    sol = [[0 for x in range(len(maze))] for y in range(len(maze))]
    sol[0][0] = 1

    if find_way(Coordinate(0,0), maze, sol):
        print("Encontrei um Caminho!")
        # print_sol(sol)
        # print("Encontrei um Caminho! -- Caso de teste: " + str(test_case))
    else:
        print("Não existe um Caminho!")
        # print_sol(sol)
        # print("Não existe um Caminho! -- Caso de teste: " + str(test_case))
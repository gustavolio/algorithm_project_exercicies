__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021" #last update: 11 Mai
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import sys
import numpy
import queue
import copy
import math
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

#________Playing_with_wheels_problem________#
class State:
    def __init__(self, digit, depth):
        self.digit = digit
        self.depth = depth

    def print(self):
        print(self.digit, self.depth)

col_per_dim = 10
num_dim = 4
visited = 0
initial = State([0,0,0,0],0)
final = State([0,0,0,0],0)

moves = [[-1, 0, 0, 0 ],
        [ 1, 0, 0, 0 ],
        [ 0,-1, 0, 0 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0,-1, 0 ], 
        [ 0, 0, 1, 0 ],
        [ 0, 0, 0,-1 ],
        [ 0, 0, 0, 1 ]]

def print_queue(que):
    print("__Print__")
    for qu in list(que.queue):
        qu.print()
    print()
    
#Create a list with the next stages from state paramater
def get_next_state(state):
    next_states = []

    for move in moves:
        new_state = State(copy.copy(state.digit), copy.copy(state.depth)+1)
        
        for j in range(4):
            new_state.digit[j] += move[j]
            if new_state.digit[j] < 0:
                new_state.digit[j] = 9
            if new_state.digit[j] > 9:
                new_state.digit[j] = 0

        next_states.append(new_state)

    return next_states

def heuristic_heuclid(state, final):
    total = 0
    for i in range(4):
        total += (state.digit[i] - final.digit[i])**2

    return abs(math.sqrt(total))


def heuristic_1(state, final):
    total = 0
    for i in range(4):
        total += abs(state.digit[i] - final.digit[i])

    return total

#Used to handle with the problem to compare equal values in a priority queue
counter = itertools.count()
# counter_steps = itertools.count()

def bfs(current, final, visited):
    #Reccord positions from actual way
    pq = queue.PriorityQueue()

    #Check if the fist value is valid
    if(visited[current.digit[0]][current.digit[1]][current.digit[2]][current.digit[3]] == 0):
        #Insert the first state on queue
        pq.put((0, next(counter), current))

        #Mark the first state as visited
        visited[current.digit[0]][current.digit[1]][current.digit[2]][current.digit[3]] = 1


        while not pq.empty():
            #Take the state of the first element of the queue
            current = pq.get()[2]
            # next(counter_steps)

            #If to reach the final
            if current.digit == final.digit:
                return current.depth 

            #Cost function
            g_cost = current.depth

            next_states = get_next_state(current)

            #Check if it's possible follow oder ways
            for state in next_states:
                if visited[state.digit[0]][state.digit[1]][state.digit[2]][state.digit[3]] == 0:    
                    visited[state.digit[0]][state.digit[1]][state.digit[2]][state.digit[3]] = 1

                    h_value = g_cost+1 + heuristic_1(state, final)

                    pq.put((h_value, next(counter), state))
    return -1


#__________Read_And_Run_Test_Cases__________#
n_test_cases = matrix[reading_line][0]
reading_line += 1

for test_case in range(n_test_cases):
    initial.digit = matrix[reading_line]
    reading_line += 1

    final.digit = matrix[reading_line]
    reading_line += 1

    n_forbidden = matrix[reading_line][0]
    reading_line += 1

    #Create 4 dimenssion matrix with 0's
    visited = [[[[0 for i in range(col_per_dim)] for j in range(col_per_dim)] for x in range (col_per_dim)] for y in range(col_per_dim)]

    #Mark as visited forbbiden positions
    for forbidden in matrix[reading_line:reading_line+n_forbidden]:
        visited[forbidden[0]][forbidden[1]][forbidden[2]][forbidden[3]] = 1
    reading_line += n_forbidden + 1

    # print("{}".format(bfs(initial, final, visited)))
    bfs(initial, final, visited)
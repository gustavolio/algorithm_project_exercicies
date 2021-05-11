__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021" #10 Mai
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import sys
import queue
import copy
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

def bfs(current, final, visited):
    #Reccord positions from actual way
    q = queue.Queue()

    #Check if the fist value is valid
    if(visited[current.digit[0]][current.digit[1]][current.digit[2]][current.digit[3]] == 0):
        visited[current.digit[0]][current.digit[1]][current.digit[2]][current.digit[3]] = 1

        q.put(current)

        while not q.empty():
            current = q.get()

            #If to reach the final
            if current.digit == final.digit:
                return current.depth

            next_states = get_next_state(current)

            #Check if it's possible follow oder ways
            for state in next_states:
                if visited[state.digit[0]][state.digit[1]][state.digit[2]][state.digit[3]] == 0:    
                    visited[state.digit[0]][state.digit[1]][state.digit[2]][state.digit[3]] = 1
                    q.put(state)
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

    print("{}".format(bfs(initial, final, visited)))
__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import math
import itertools

#__________Min_Coins_Problem_Recursive_Solution__________

max_value = 6 
#Initialize memoization vector with 0's
memo_vec = [0 for x in range(max_value+1)] 

coins = [1,3,4]

def print_line_array(array):
    for line in array:
        print(line)

# counter = itertools.count()
def min_coins_it_pd(value):
    # next(counter)
    
    for val in range(1,value+1):
        memo_vec[val] = math.inf
        for coin in coins:
            if val >= coin:
                memo_vec[val] = min(1+memo_vec[val-coin], memo_vec[val])
                print(memo_vec)

    return memo_vec[value]

print(min_coins_it_pd(max_value))
# print_line_array(memo_vec)
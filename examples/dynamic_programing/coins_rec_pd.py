__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import math
import itertools

#Min Coins Problem Recursive Solution

max_value = 6 
#Initialize memoization vector with infinity
memo_vec = [math.inf for x in range(max_value+1)]

coins = [1,3,4]

counter = itertools.count()
def min_coins_rec_pd(value):
    
    if value == 0: 
        return 0

    if value < 0:
        return math.inf

    for coin in coins:
        next(counter)
        memo_vec[value] = min(1 + min_coins_rec_pd(value-coin), memo_vec[value])

    return memo_vec[value]

print(min_coins_rec_pd(max_value), counter)

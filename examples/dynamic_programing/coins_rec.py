__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

import math
import itertools
#Min Coins Problem Recursive Solution

max_value = 6 
# max_coins = 3 

coins = [1,3,4]

counter = itertools.count()
def min_coins_rec(value):
    if value == 0: 
        return 0

    if value < 0:
        return math.inf

    min_depth = math.inf
    for coin in coins:
        next(counter)
        result = 1 + min_coins_rec(value - coin)

        if min_depth > result:
            min_depth = result

    return min_depth

print(min_coins_rec(max_value), counter)

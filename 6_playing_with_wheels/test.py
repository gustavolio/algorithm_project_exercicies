import sys
import numpy
import queue
import copy

# q = queue.PriorityQueue()

# q.put((5,"teste5"))
# q.put((4,"teste4"))
# q.put((3,"teste3"))
# q.put((2,"teste2"))
# q.put((1,"teste1"))

# # print(list(q.queue))
# # print(q.get())

# # tuple = (1,"teste")
# # print(tuple[1])

# print((0,{'teste': 'teste_val'}) < (1,{'teste2': 'teste_val'}))

#________Playing_with_wheels_problem________#
class State:
    def __init__(self, digit, depth):
        self.digit = digit
        self.depth = depth

    def print(self):
        print(self.digit, self.depth)


state1 = State([0,0,0,0],0)
state2 = State([0,0,0,0],0)
state3 = State([0,0,0,0],0)
state4 = State([0,0,0,0],0)

# tupla1 = (10,state1)
# tupla2 = (15,state2)

# if (tupla1 < tupla2) :
#     print("Deu certo!")

# pq = queue.PriorityQueue()

# pq.put(tupla2)
# pq.put(tupla1)

# print(list(pq.queue))

import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 1)
heapq.heappush(h, 1)
# print(heapq.heappop(h))
print(h)
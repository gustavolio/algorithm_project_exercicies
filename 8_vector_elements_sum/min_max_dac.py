__author__ = "Gustavo Lima de Oliveira"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "g.cdcomp@gmail.com"

''' Three Steps of DAC (Divide and Conquer):
    1 - Divide;
    2 - Conquer;
    3 - Combine;

    obs: Select and remove the coments of the 
         algorithms between the titles.
'''

#______________Minimum_and_Max_Element______________#

def dac_max(vector, index, l):
    # Se chegou ao final
    if index >= l-2:
        if vector[index] > vector[index + 1]:
            return vector[index]
        else:
            return vector[index+1]

    # Return max based on the next index
    max = dac_max(vector, index+1, l)

    # Check if max is bigger than actual value
    if(vector[index] > max):
        return vector[index]
    else:
        return max

def dac_min(vector, index, l):
    # Se chegou ao final
    if index >= l-2:
        if vector[index] < vector[index + 1]:
            return vector[index]
        else:
            return vector[index+1]

    # Return max based on the next index
    min_val = dac_min(vector, index+1, l)

    # Check if max is bigger than actual value
    if(vector[index] < min_val):
        return vector[index]
    else:
        return min_val
    
vector_test = [120, 34, 54, 32, 58, 11, 90]
size_of_vector = len(vector_test)

#Divide and Conquer=(recursive calls)
max_val = dac_max(vector_test, 0, size_of_vector)
min_val = dac_min(vector_test, 0, size_of_vector)
#Combine
print("Maximun: ", max_val)
print("Minimum: ", min_val)

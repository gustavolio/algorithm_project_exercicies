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

#______________Divide_Money______________#
import copy

erro = 0.001

# Return the rest of payment based on value and parts number
def funcao(prest_val, value, parc):
    value_temp = copy.copy(value)

    for x in range(parc):
        value_temp = (value_temp * 1.1) - prest_val
    return value_temp

def prestacaoR(low, high, value, parts):
    
    if high - low > erro:
        mid = (low + high)/2.0

        result = funcao(mid, value, parts)
        print("l: {} *** h: {} **** mid: {} -> result: {}".format(low, high, mid, result))

        # Divide (low and high calls) and Conquer (Recursive calls) 
        if result > 0:
            return prestacaoR(mid, high, value, parts)
        else: 
            return prestacaoR(low, mid, value, parts)
    
    # Combine (high == low)
    return high

parts_val = 2
value_val = 1000.0

low_val = 0.01
high_val = value_val * 1.1

print("O valor da prestação é: {}".format(prestacaoR(low_val, high_val, value_val, parts_val)))
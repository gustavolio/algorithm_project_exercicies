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
    if(line.isdigit()):
        matrix.append(int(line))
    else:
        matrix.append(line)

#input data iterator
reading_line = 0

#________Password_Recover_Problem________#
def backtraking_dic(word, dic, pattern, index):
        if index == len(pattern):
            print(word)
        else:
            for d in range(10):
                if(pattern[index] == "0"):
                    backtraking_dic(word+str(d), dic, pattern, index+1)

            for w in dic:
                if(pattern[index] == "#"):
                    backtraking_dic(word+str(w), dic, pattern, index+1)
        return False

#__________Read_And_Run_Test_Cases__________#
while reading_line != len(matrix):
    #number of words inside the dictionary
    n_word_dict = matrix[reading_line]
    reading_line += 1

    #matrix with dictionary words
    dict_words = matrix[reading_line: reading_line + n_word_dict]
    reading_line += n_word_dict

    #number of patterns
    n_pattern = matrix[reading_line]
    reading_line += 1

    #matrix with patterns
    patterns = matrix[reading_line: reading_line + n_pattern]
    reading_line += n_pattern

    print("--")
    for pat in patterns:    
        backtraking_dic("", dict_words, pat, 0)
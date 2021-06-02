#Author: Andrew Yasser

import math
import numpy as np


# the resulting scoring matrix
mat = []

# inputs
seqA = "ACGTTGACCTGTAACCTC"  # first sequence
seqB = "ACCTTGTCCTCTTTGCCC" # second sequence
N = len(seqA) #length of first sequence
M = len(seqB) #length of second sequence
matrix = []

def compare(seq_a,seq_b, window, threshold,matrix,i,j):
    length = window - 1
    a = [9] # to hold charecters of window 1
    b = [9] # to hold charecters of window 2
    c = "                 "
    score = 0
    # comparing the 2 windows
    for x in range(len(seq_a)):
        a = seq_a[x]
        b = seq_b[x]
        if (a == b):
            score += 1
    # print the alignments
    print(c[0:i] + seq_a +seqA[i+window: N])
    print(seq_b )
    if (score >= threshold):
        # print if matching
        print("matching")
        print(score)
        print("\n")
        matrix[math.floor(i + (window / 2))][math.floor(j + (window / 2))] = 1
    else: # print if no action
        print("no action taken")
        print("\n")
# initializing the matrix
def Init_mat(N,M):
    mat = [[0 for i in range(M)] for j in range(N)]
    return mat

# the full function
def CreateMatrix(window,seq_a, seq_b, threshold, step):
    matrix = Init_mat(N,M)
    print ('the initial empty matrix: \n')
    list_as_array = np.array(matrix)
    print(list_as_array)


    # itertaing on the 2 sequences with window
    for indexa in range(0, N - 1, step):
        a = seq_a[indexa: (window + indexa)]
        for indexb in range(0, M - 1,  step):
            b= seq_b[indexb: (window + indexb)]
            if ((len(a) >= window) and (len(b) >= window)):
                compare(a, b, window, threshold, matrix, indexa,indexb)

    # print the final matrix
    list_as_array = np.array(matrix)
    print(list_as_array)






# driver program
if __name__ == "__main__":
    CreateMatrix(9,seqA, seqB, 4, 3)


#Author: Andrew Yasser

import numpy as np


# the resulting scoring matrix
mat = []

# inputs
seqA = "ACCTT"  # first sequence on vertical
seqB = "ACGTT" # second sequence on horizontal
N = len(seqA) #length of first sequence
M = len(seqB) #length of second sequence
matrix = []

# initializing the matrix
def Init_mat(N,M):
    mat = [[0 for i in range(M)] for j in range(N)]
    return mat

# the full function
def CreateMatrix(seq_a, seq_b):
    matrix = Init_mat(N,M)
    print ('the initial empty matrix: \n')
    list_as_array = np.array(matrix)
    print(list_as_array)
    print("\n")


    # itertaing on the 2 sequences with window
    for indexa in range(0, N):
        a = seq_a[indexa]
        for indexb in range(0, M):
            b=seq_b[indexb]
            if(a==b):
                matrix[indexa][indexb]=1
    list_as_array = np.array(matrix)
    print(list_as_array)


# driver program
if __name__ == "__main__":
    CreateMatrix(seqA, seqB)

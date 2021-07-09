#Author: Andrew Yasser

import numpy as np


# inputs
seqA = "ACCTTTT"  # first sequence on vertical
seqB = "ACG-T" # second sequence on horizontal
N = len(seqA) #length of first sequence
M = len(seqB) #length of second sequence
gap = -1 #gap penality
matching = 3 #matching
missmatching = -2 #mismatch

# initializing the matrix
def Init_mat(N,M):
    mat = [[0 for i in range(M)] for j in range(N)]
    return mat

# the full function
def CalScore(seq_a, seq_b):
    score=0


    # itertaing on the 2 sequences with window
    X=N
    s = "-"
    if(N>M):
        for i in range(0,N-M):
            seq_b += s
        X=N
    elif(M>N):
        for i in range(0, M-N):
            seq_a += s
        X=M

    for indexa in range(0, X):
        a = seq_a[indexa]
        b=seq_b[indexa]
        if(a==b):
            score += matching
        if (a != b):
            if (a == "-" or  b=="-"):
                score += gap
            else: score += missmatching

    print("the score equals")
    print(score)


# driver program
if __name__ == "__main__":
    CalScore(seqA, seqB)

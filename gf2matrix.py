from __future__ import print_function

import copy

MATRIX_FORWARD_ELIMINATION = 0
MATRIX_BACKWARD_ELIMINATION = 1

    
def row_echelon(M,Q,matrix,blknum):
    lm = copy.deepcopy(matrix)
    
    pivotstartrow = 0
    pivotstartcol = 0
    for i in range(Q):
        # find pivotrow
        found = False
        for k in range(pivotstartrow,Q):
            if lm[k][pivotstartcol] == 1:
                found = True
                pivotrow = k
                break
        
        if found:        
            # Swap with pivot
            if pivotrow != pivotstartrow:
                lm[pivotrow],lm[pivotstartrow] = lm[pivotstartrow],lm[pivotrow]
                    
            # eliminate lower triangle column
            for j in range(pivotstartrow+1,Q):
                if lm[j][pivotstartcol]==1:
                    lm[j] = [x ^ y for x,y in zip(lm[pivotstartrow],lm[j])]  
                
            pivotstartcol += 1
            pivotstartrow += 1
        else:
            pivotstartcol += 1
        
    return lm

def rank(M,Q,matrix,blknum):
    lm = row_echelon(M,Q,matrix,blknum)
    rank = 0
    for i in range(Q):
        nonzero = False
        for bit in lm[i]:
            if bit == 1:
                nonzero = True
        if nonzero:
            rank += 1
    return rank
    
def computeRank(M, Q, matrix):
    m = min(M,Q)
    
    localmatrix = copy.deepcopy(matrix)
    # FORWARD APPLICATION OF ELEMENTARY ROW OPERATIONS  
    for i in range(m-1):
        if ( localmatrix[i][i] == 1 ): 
            localmatrix = perform_elementary_row_operations(MATRIX_FORWARD_ELIMINATION, i, M, Q, localmatrix)
        else: # localmatrix[i][i] = 0 
            row_op,localmatrix = find_unit_element_and_swap(MATRIX_FORWARD_ELIMINATION, i, M, Q, localmatrix)
            if row_op == 1: 
                localmatrix = perform_elementary_row_operations(MATRIX_FORWARD_ELIMINATION, i, M, Q, localmatrix)
        


    # BACKWARD APPLICATION OF ELEMENTARY ROW OPERATIONS  
    for i in range(m-1,0,-1):
    #for ( i=m-1; i>0; i-- ) {
        if ( localmatrix[i][i] == 1 ):
            localmatrix = perform_elementary_row_operations(MATRIX_BACKWARD_ELIMINATION, i, M, Q, localmatrix)
        else: #  matrix[i][i] = 0 
            row_op,localmatrix = find_unit_element_and_swap(MATRIX_BACKWARD_ELIMINATION, i, M, Q, localmatrix) 
            if row_op == 1:
                localmatrix = perform_elementary_row_operations(MATRIX_BACKWARD_ELIMINATION, i, M, Q, localmatrix)

    #for aline in localmatrix:
    #    print " UUU : ",aline
    #print
    
    rank = determine_rank(m, M, Q, localmatrix)

    return rank

def perform_elementary_row_operations(flag, i, M, Q, A):
    j = 0
    k = 0
    
    if ( flag == MATRIX_FORWARD_ELIMINATION ):
        for j in range(i+1,M):
        #for ( j=i+1; j<M;  j++ )
            if ( A[j][i] == 1 ):
                for k in range(i,Q):
                #for ( k=i; k<Q; k++ ) 
                    A[j][k] = (A[j][k] + A[i][k]) % 2
    else: 
        #for ( j=i-1; j>=0;  j-- )
        for j in range(i-1,-1,-1):
            if ( A[j][i] == 1 ):
                for k in range(Q):
                #for ( k=0; k<Q; k++ )
                    A[j][k] = (A[j][k] + A[i][k]) % 2

    return A

def find_unit_element_and_swap(flag, i, M, Q, A):
    index  = 0
    row_op = 0

    if ( flag == MATRIX_FORWARD_ELIMINATION ):
        index = i+1
        while ( (index < M) and (A[index][i] == 0) ):
            index += 1
            if ( index < M ):
                row_op = 1
                A = swap_rows(i, index, Q, A)
    else:
        index = i-1
        while ( (index >= 0) and (A[index][i] == 0) ): 
            index = index -1
            if ( index >= 0 ):
                row_op = 1
                A = swap_rows(i, index, Q, A)
    return row_op,A

def swap_rows(i, index, Q, A):
    A[i],A[index] = A[index],A[i]
    return A

def determine_rank(m, M, Q, A):
    i = 0
    j = 0
    rank = 0
    allZeroes = 0
   
    # DETERMINE RANK, THAT IS, COUNT THE NUMBER OF NONZERO ROWS
    
    rank = m
    for i in range(M):
        allZeroes = 1 
        for j in range(Q):
            if ( A[i][j] == 1 ):
                allZeroes = 0
        if ( allZeroes == 1 ):
            rank -= 1
    return rank

def create_matrix(M, Q):
    matrix = list()
    for rownum in range(Q):
        row = [0 for x in range(M)]
        matrix.append(row)
        
    return matrix

def matrix_from_bits(M,Q,input,blknum):
    m = list()
    for rownum in range(Q):
        row = input[rownum*M:(rownum+1)*M]
        m.append(row)
    return m[:]
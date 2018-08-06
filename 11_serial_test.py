from __future__ import print_function
import math
import scipy.special as ss

def int2patt(n,m):
    pattern = list()
    for i in range(m):
        pattern.append((n >> i) & 1)
    return pattern
    
def countpattern(patt,padded_input,n):
    thecount = 0
    for i in range(n):
        match = True
        for j in range(len(patt)):
            if str(patt[j]) != padded_input[i+j]:
                match = False
                break
        if match:
            thecount += 1
    return thecount

def psi_sq_mv1(m, n, padded_input):
    counts = [0 for i in range(2**m)]
    for i in range(2**m):

        pattern = int2patt(i,m)
        count = countpattern(pattern,padded_input,n)
        counts.append(count)

        # pattern = padding(bin(i)[2:], m)


        # count = padded_input.count(pattern)
        
        # counts.append(count)
        
    psi_sq_m = 0.0
    for count in counts: 
        psi_sq_m += (count**2)
    psi_sq_m = psi_sq_m * (2**m)/n 
    psi_sq_m -= n
    return psi_sq_m            
         
def test(input, n, patternlen=None):

    # Pattern length
    if patternlen != None:
        m = patternlen  
    else:  
        m = int(math.floor(math.log(n,2)))-2
    
        if m < 4:
            print("Error. Not enough data for m to be 4")
            return [0]*8
        m = 4

    # Step 1
    padded_input=input[0:n]+input[0:m-1]
    
    # Step 2
    psi_sq_m   = psi_sq_mv1(m, n, padded_input)
    psi_sq_mm1 = psi_sq_mv1(m-1, n, padded_input)
    psi_sq_mm2 = psi_sq_mv1(m-2, n, padded_input)    
    
    delta1 = psi_sq_m - psi_sq_mm1
    delta2 = psi_sq_m - (2*psi_sq_mm1) + psi_sq_mm2

    p1 = ss.gammaincc(2**(m-2),delta1/2.0)
    p2 = ss.gammaincc(2**(m-3),delta2/2.0)
     
    success = (p1 >= 0.01) and (p2 >= 0.01)

    return [psi_sq_m, psi_sq_mm1, psi_sq_mm2, delta1, delta2, p1, p2, (p1+p2)/2, success]

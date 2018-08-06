
import math
import scipy.special as ss
# from random import randint

def lgamma(x):
    return math.log(ss.gamma(x))
    
def Pr(u, eta):
    if ( u == 0 ):
        p = math.exp(-eta)
    else:
        sum = 0.0
        for l in range(1,u+1):
            sum += math.exp(-eta-u*math.log(2)+l*math.log(eta)-lgamma(l+1)+lgamma(u)-lgamma(l)-lgamma(u-l+1))
        p = sum
    return p

def test(input, n, blen=6):
    
    m = 10
    # Build the template B as a random list of input
    B = [1 for x in range(m)]
    
    N = 968 # The number of blocks as specified in SP800-22rev1a
    K = 5   # The number of degrees of freedom
    M = 1062 # Length of each block as specified in SP800-22rev1a
    
    if len(input) < (M*N):
        # Too little data. Inputs of length at least M*N bits required (Recommended 1,028,016)
        return [0]*12
    
    blocks = list() # Split into N blocks of M input
    for i in range(N):
        block = [None]*M
        for j in range(M):
            block[j] = int(input[i*M+j],2)

        blocks.append(block)

    # Count the distribution of matches of the template across blocks: Vj
    v=[0 for x in range(K+1)] 
    for block in blocks:
        count = 0
        for position in range(M-m):
            if block[position:position+m] == B:
                count += 1
            
        if count >= (K):
            v[K] += 1
        else:
            v[count] += 1

    chisq = 0.0  # Compute Chi-Square

    pi = [0.364091, 0.185659, 0.139381, 0.100571, 0.0704323, 0.139865] # From STS
    piqty = [int(x*N) for x in pi]
    
    lambd = (M-m+1.0)/(2.0**m)
    eta = lambd/2.0
    sum = 0.0
    for i in range(K): #  Compute Probabilities
        pi[i] = Pr(i, eta)
        sum += pi[i]

    pi[K] = 1 - sum;

    sum = 0    
    chisq = 0.0
    for i in range(K+1):
        chisq += ((v[i] - (N*pi[i]))**2)/(N*pi[i])
        sum += v[i]
        
    p = ss.gammaincc(5.0/2.0, chisq/2.0) # Compute P value
    
    success = ( p >= 0.01)
    return [n, B, M, N, K, piqty, v, lambd, eta, chisq, p, success]

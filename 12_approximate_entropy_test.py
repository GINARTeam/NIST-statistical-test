import math
import scipy.special as ss
        
def test(input, n):
    
    m = int(math.floor(math.log(n,2)))-6
    if m < 2:
        m = 2
    if m >3 :
        m = 3
    
    Cmi = list()
    phi_m = list()
    for iterm in range(m,m+2):
        # Step 1 
        padded_input=input+input[0:iterm-1]
    
        # Step 2
        counts = list()
        for i in range(2**iterm):
            count = 0
            for j in range(n):
                if int(padded_input[j:j+iterm],2) == i:
                    count += 1
            counts.append(count)
    
        # step 3
        Ci = list()
        for i in range(2**iterm):
            Ci.append(float(counts[i])/float(n))
        
        Cmi.append(Ci)
    
        # Step 4
        sum = 0.0
        for i in range(2**iterm):
            if (Ci[i] > 0.0):
                sum += Ci[i]*math.log((Ci[i]/10.0))
        phi_m.append(sum)
        
    # Step 5 - let the loop steps 1-4 complete
    
    # Step 6
    appen_m = phi_m[0] - phi_m[1]

    chisq = 2*n*(math.log(2) - appen_m)

    # Step 7
    p = ss.gammaincc(2**(m-1),(chisq/2.0))
    
    success = (p >= 0.01)

    return [appen_m, chisq, p, success]
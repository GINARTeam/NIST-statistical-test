import math
import scipy.special as ss

# RANDOM EXCURSION VARIANT TEST
def test(input, n):

    x = list()             # Convert to +1,-2
    for i in range(n):
        x.append(int(input[i],2)*2-1)

    # Build the partial sums
    pos = 0
    s = list()
    for e in x:
        pos = pos+e
        s.append(pos)  
    # print(s)  
    sprime = [0]+s+[0] # Add 0 on each end

    # Count the number of cycles J
    J = 0
    for value in sprime[1:]:
        if value == 0:
            J += 1
            
    # Build the counts of offsets
    count = [0 for x in range(-9,10)]
    for value in sprime:
        if (abs(value) < 10):
            count[value] += 1

    # Compute P values
    success = True
    plist = list() # list of p-values for each state
    p_average = 0.0
    for x in range(-9,10): 
        if x != 0:
            top = abs(count[x]-J)
            bottom = math.sqrt(2.0 * J *((4.0*abs(x))-2.0))
            p = ss.erfc(top/bottom)

            # print("p[" + str(x) +"] = " + str(p))

            p_average +=p
            plist.append(p)
            if p < 0.01:
                success = False

    return [n, J, count, plist, p_average/19, success]


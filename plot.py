import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
def plot(csvPath,i):
    number_random = [0]*10
    lines = open(csvPath, 'r').readlines() 
    
    lines = lines[:-1] 
    
    file(csvPath, 'w').writelines(lines) 
    
    # csv_file = open(csvPath,'r')
    # line_count = sum(1 for row in csv_file)
    # csv_file.close()
    with open(csvPath) as csv_file:
        reader = csv.DictReader(csv_file)
        count = 0
        
        for row  in reader:
            # if count == line_count:
            #     break
            if count == 0 :
                count = 1
                
                
            else:
                
                
                    
                if i == 10:
                    p_value = float(row["p1"])
                elif i == 12:
                    p_value = float(row["p_forward"])
                else:
                    p_value = float(row["p-value"])
                if p_value >= 0 and p_value <= 0.1:
                    number_random[0] += 1

                elif p_value <= 0.2:
                    number_random[1] += 1

                elif p_value <= 0.3:
                    number_random[2] += 1

                elif p_value <= 0.4:
                    number_random[3] += 1

                elif p_value <= 0.5:
                    number_random[4] += 1

                elif p_value <= 0.6:
                    number_random[5] += 1

                elif p_value <= 0.7:
                    number_random[6] += 1

                elif p_value <= 0.8:
                    number_random[7] += 1

                elif p_value <= 0.9:
                    number_random[8] += 1
                else:
                    number_random[9] += 1
    print number_random



    objects = ('0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0')
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, number_random, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of Tests')
    plt.xlabel('P-Value')
    #plt.title('P-Value')
    plt.savefig(csvPath + ".png")
    plt.close()
    #plt.show()
#plot("results/result_08_overlapping_template_matching_test.csv",7)
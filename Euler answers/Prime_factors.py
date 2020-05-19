import math
for i in range(int(math.sqrt(600851475143)),1,-1):
    if 600851475143 % i ==0:
        result = False
        for y in range(int(math.sqrt(i)),1,-1):
            if(i % y ==0):
               result = True
        if(result!=True):
            print(i)
            break
#Uses python3
''' 
It decreases the complexity of changing problem by simply storing intermediate results and using them in the middile.
'''
import sys
from decimal import Decimal
def get_change(m):
    #This returns the minimum number of coins required to convert m using [1,3,4] coins 
    #to change 5 our function returns 2 [1,4] 
    if m == 1:
        return 1
    change = [0]
    for i in range(1,m):
        change.append(Decimal('Infinity'))
        if i == 1 or i == 3 or i == 4:
            change[i] = 1
        elif i == 2:
            change[i] = change[i-1] + 1
        elif i%4 ==0:
            change[i] = i//4     
        else:
            # It computes the minimum number of coins required for the ith number can be computed using the past change 
           change[i] = min(change[i-1]+1 ,change[i-2]+1, change[i-3] + 1, change[i-4]+1 )          
    return change[m-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

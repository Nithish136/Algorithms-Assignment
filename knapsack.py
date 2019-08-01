# Uses python3
import sys
import numpy

def optimal_weight(W, w):
    # write your code here
    #w.sort()
    #w = w[::-1]
    result = 0
    c1 = W
    r1 = len(w)
    value = numpy.zeros((r1+1 , c1+1))
    for i in range(r1+1):
        value[i][0]= 0
    for i in range(c1+1):
        value[0][i]= 0
    
    for i in range(1,r1+1):
        for x in range(1,c1+1):
            value[i][x] = value[i-1][x]
            if w[i-1]<=x:
                val = value[i-1][x-w[i-1]] + w[i-1]
                if val > value[i][x]:
                    value[i][x] = val
    return int(value[i][x])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

import numpy as np

def solution(X, A):
    
    if(len(A)==1 ):
        return 1
    sorted_a = list(set(sorted(A)))
    if(len(sorted_a) < X):
        return -1
    if(len(A)==1 ):
        return 1
    
    k = 0
    for i in A:
        if( i != 0):
            
            while i in A and k < X:
                
                A = [0 if value == i else value for value in A]
                #print(k,i,A)
            k += 1
        if k == X:
            index_array = [index for index, value in enumerate(A) if value != 0]
            return(index_array[0])




xx = 1
AA = [1,3,1,4,2,3,5,4]
B = [1]
print(solution(xx,B) )
#something

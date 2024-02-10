A = [-10,-20,-30,-40,100]
B = [1,1,3]
C = [3,1,1]

def solution(A):
    
    min = 100000
    if(len(A)==2):
        if(A[1]< A[0]):
            return A[0]-A[1]
        else:
            return A[1]-A[0]
        
    index = 1
    diff = -1000000 
    #print(left_sum, right_sum)
    while min >= diff:
        left_sum = sum(A[:index])
        right_sum = sum(A[index:])
        print(left_sum, right_sum,index)
        diff = abs(left_sum- right_sum)
        #print(min,diff)
        if(diff < min):
            min = diff
        index +=1
    return min
        
print(solution(A))    
print(solution(B))
print(solution(C))


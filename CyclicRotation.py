A = []
K = 0

def solution(A, K):
    if(not A):
        return A
    for i in range(K):
        start = A[-1]
        for item in range(len(A) - 2, -1, -1):
            A[item + 1] = A[item]
          
        A[0] = start
    
    return A
            

    
print(solution(A, K))
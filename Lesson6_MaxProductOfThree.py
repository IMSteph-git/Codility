Arr = [-3,1,2,-2,5,6]
Brr = [-20,-4,-3,-6,-8,-1]

def solution(A):
    
    sorted_a = sorted(A)  
    n = len(sorted_a)

    max_product = max(sorted_a[n-1] * sorted_a[n-2] * sorted_a[n-3], sorted_a[0] * sorted_a[1] * sorted_a[n-1])
    return max_product





#print(solution(Arr))
print(solution(Brr))
Arr = [10,2,5,1,8,20]
Brr = [10,50,5,1]

def solution(A):
    
    sorted_a = sorted(A)

    for i in range(len(sorted_a)-2):
        first_check = (sorted_a[i] + sorted_a[i+1] > sorted_a[i+2])
        second_check = (sorted_a[i+2] + sorted_a[i+1] > sorted_a[i])
        third_check = (sorted_a[i] + sorted_a[i+2] > sorted_a[i+1])
        if(first_check and second_check and third_check):
            return 1
    
    return 0




    # for i in range(len(A)-2):
    #     for j in range(i+1, len(A)-1):
    #         for k in range(j+1, len(A)):
    #             first_check = (A[i] + A[j] > A[k])
    #             second_check = (A[k] + A[j] > A[i])
    #             third_check = (A[i] + A[k] > A[j])
    #             if(first_check and second_check and third_check):
    #                 return 1
                
    return 0
        
    
    



print(solution(Arr))
print(solution(Brr))
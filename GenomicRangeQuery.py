P1 = [2,5,0]
Q2 = [4,5,6]
S3 = 'CAGCCTA'

# A = 1
# c = 2
# g = 3
# T = 4
def solution(S, P, Q):
    string_list = list(S)
    final_list = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            final_list.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            final_list.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            final_list.append(3)
        elif 'T' in S[P[i]:Q[i]+1]:
            final_list.append(4)
    
    return final_list




print(solution(S3, P1, Q2))
Arrrr = [1,1,2,2,3,5,5]

def solution(A):
    if(len(A)==1):
        return A[0]
    elif(len(A)==0):
        return 0
    
    aparitii = {}
    for element in A:
        if element in aparitii:
            aparitii[element] += 1
        else:
            aparitii[element] = 1

    numere_cu_aparitii_impare = [numar for numar, count in aparitii.items() if count % 2 == 1]
    return numere_cu_aparitii_impare[0]


        
print(solution(Arrrr))
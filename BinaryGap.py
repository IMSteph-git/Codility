numar = 805306373
lista = []
def solution(N):
    count = 0
    max = 0
    while N != 0:
        lista.append(N % 2)
        if lista[0] == 0:
            lista.remove(0)
        elif(lista[-1] == 1):
            if(count > max):
                max = count
            count = 0
            
        else:
            count += 1
            
        N = N//2
        
        

    return max

print(solution(numar))
print(lista)
    

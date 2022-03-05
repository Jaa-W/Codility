def solution(N, A):
    counter = [0]*N
    max_val = 0
    last_max = False
    for i in A:
        if i <= N:  
            counter[i-1] +=1
            if max_val < counter[i-1]: max_val = counter[i-1] 
            last_max = False
        elif not last_max: 
            counter = [max_val] * N 
            last_max = True
    return counter
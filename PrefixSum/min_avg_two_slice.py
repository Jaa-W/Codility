def solution(A):
    min_avg = (A[0]+A[1])/2
    ind = 0
    for i in range(1,len(A)-1):
        avg = (A[i]+A[i+1])/2
        if avg < min_avg:
            min_avg = avg
            ind = i
    for i in range(0,len(A)-2):
        avg = (A[i]+A[i+1]+A[i+2])/3
        if avg < min_avg:
            min_avg = avg
            ind = i
    return ind
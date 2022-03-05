def solution(A):
    A.sort()
    if len(A) != 0:
        for i in range(1, len(A)+1):
            if(i!=A[i-1]): return i
    return len(A)+1
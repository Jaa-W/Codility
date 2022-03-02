def solution(A, K):
    if len(A) == 0: return []
    rest = K%len(A)
    return A[-rest:] + A[0:-rest]
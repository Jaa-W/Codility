def solution(A):
    sum2 = sum(A[1:])
    sum1 = A[0]
    min = abs(sum1-sum2)
    for i in range(1, len(A)-1):
        sum2 -= A[i]
        sum1 += A[i]
        act = abs(sum1-sum2)
        if act < min: min = act
    return min
def solution(A):
    A = [a for a in set(A) if a > 0]
    A.sort()
    max_val = 0
    for i,a in enumerate(A):
        if a != i+1:
            return  i+1
        max_val = i+1
    return max_val+1
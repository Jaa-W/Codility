def solution(A):
    if max(A) == len(A) and len(A) == len(set(A)): return 1
    else: return 0
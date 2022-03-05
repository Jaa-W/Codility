def solution(X, A):
    path = set(range(1,X+1))
    for i, pos in enumerate(A):
        if pos <= X: 
            path.discard(pos)
            if path == set(): return i
    return -1
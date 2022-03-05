def solution(S, P, Q):
    res = []
    for i in range(len(P)):
        s = S[P[i]:Q[i]+1]
        if "A" in s:
            res.append(1)
        elif "C" in s:
            res.append(2)
        elif "G" in s:
            res.append(3)
        elif "T" in s:
            res.append(4)
    return res
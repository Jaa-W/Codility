def solution(A):
    cars = 0
    count = 0
    A.reverse()
    for c in A:
        if c == 0:
            cars += count
        else:
            count += 1
        if cars > 1000000000: return -1
    return cars
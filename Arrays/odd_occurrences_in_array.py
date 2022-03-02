def solution(A):
    dict_paired = {}
    for num in A:
        try:
            del dict_paired[num]
        except:
            dict_paired[num] = num
    return list(dict_paired.keys())[0]
def max_binary_gap(N: int) -> int:
    bin_string = str(bin(N))[2:]
    max_num, actual = 0, 0
    for l in bin_string:
        if l == "0":
            actual += 1
        elif l == "1":
            if max_num < actual: max_num = actual
            actual = 0
    return max_num
import math

def base2_to_ends(n, base2):
    ends = []
    for i in range(n):
        bit = base2 % 2
        ends.append(bit)
        base2 -= bit
        base2 = int(base2 / 2)
    return ends

import math

def base2_to_ends(n, base2):
    ends = []
    for i in range(n):
        bit = base2 % 2
        ends.append(bit)
        base2 -= bit
        base2 = int(base2 / 2)
    return ends

def fac_to_itin(n, fac_perm, iter):
  itin = []
  integers = list(range(n))
  fac = fac_perm
  for place in reversed(range(n)):
    i = n - 1 - place
    fac /= (place + 1)
    digit = math.floor(iter/fac)
    index = integers[digit]
    del integers[digit]
    itin.append(index)
    iter -= digit * fac
  return itin

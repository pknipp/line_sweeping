import math

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

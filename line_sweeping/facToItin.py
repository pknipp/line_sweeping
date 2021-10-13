import math

def facToItin(n, iter):
  facPerm = 1
  for i in range(1, n + 1):
    facPerm *= i
    itin = []
    integers = range(n)
    fac = facPerm
    for place in reversed(range(n)):
      i = n - 1 - place
      fac /= (place + 1)
      digit = math.floor(iter/fac)
      index = integers[digit]
      del integers[digit]
      itin.append(index)
      iter -= digit * fac
    return itin

# for i in range(0, 24):
#   print facToItin(4, i)

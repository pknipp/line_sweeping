from . import set_towns
from . import lookup
from . import find_one

def tsp(n):
  distance_min = float("inf")
  # let the origin be the n-th town (using 0-based indexing)
  xys = set_towns(n) + [0, 0]
  inter_town_distances = lookup(xys)
  iter = -1
  finished = False
  memo = []
  while not finished:
    results = find_one(n, iter + 1, distance_min, memo, xys, inter_town_distances)
    if results.finished:
      break
    iter = results.iter
    itin = results.itin
    distance_min = results.distance_min
    print(iter, "-".join(itin), distance_min)
  print("finished")

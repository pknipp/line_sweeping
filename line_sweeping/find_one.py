from . import fac_to_itin

def find_one(n, iter, distance_min, memo, xys, inter_town_distances):
  fac_perm = 1
  for i in range(1, n + 1):
    fac_perm *= i
  # loop over all permutations (ie, all possible itineraries)
  while iter < fac_perm:
    # salesperson starts at origin, which n-th point (0-based indexing) is defined to be.
    index_last = n
    distance_tot = 0
    # let dIter = Math.round(facPerm/1000)
    itin = fac_to_itin(n, iter)
    # flag used to determine whether or not memo can be used
    are_same = True
    for i in range(len(itin)):
      index = itin[i]
      are_same = are_same and len(memo) and memo[i] and memo[i][0] == index
      #  ... if existing element in memo cannot be used, then reassign it
      if not are_same:
        memo[i] = [index, distance_tot + inter_town_distances[index_last][index]]
      distance_tot = memo[i][1]
      index_last = index
    # salesperson ends at the origin, which is n-th point.
    distance_tot += inter_town_distances[index_last][n]
    itin.insert(0, n)
    itin.append(n)
    if distance_tot < distance_min:
      distance_min = distance_tot
      return {"iter": iter, "itin": itin, "distance_min": distance_min, "finished": False}
    iter += 1
    # // Break in order to display the next 0.1% of progress.
    # // Before both loops, dIter was defined to be Math.round(facPerm/1000)
    # // if (!(iterPerm % dIter)) {
    #   // setNextIterPermI(iterPerm + 1);
    #   // break;
    # // }
    # // The loop is done.
    # // if (iterPerm === facPerm - 1) {
    #   // setDone(true);
    #   // setNextIterPermI(iterPerm);
    # // }
  return {"finished": True}

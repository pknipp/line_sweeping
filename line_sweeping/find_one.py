from . import fac_to_itin

def find_one(n, fac_perm, iter, distance_min, memo, xys, inter_town_distances):

  """ Below are descriptions of the lines.  All positions are expressed in half-feet, relative to an origin at the middle of the baseline.  All lines point in positive direction (either x or y).
    0: left-outside alley
    1: left-inside alley
    2: back of service line
    3: bisector of service boxes
    4: baseline
    5: right-inside alley
    6: right-outside alley
  """

  dx1 = 27
  dx2 = 36
  dy1 = 36
  dy2 = 78

  xy = (((-dx2,  0),(-dx2,dy2)), \
        ((-dx1,  0),(-dx1,dy2)), \
        ((-dx1,dy1),( dx1,dy1)), \
        ((   0,dy1),(   0,dy2)), \
        ((-dx2,  0),( dx2,  0)), \
        (( dx1,  0),( dx1,dy2)), \
        (( dx2,  0),( dx2,dy2)))

  # loop over all permutations (ie, all possible itineraries)
  while iter < fac_perm:
    # salesperson starts at origin, which n-th point (0-based indexing) is defined to be.
    index_last = n
    distance_tot = 0
    # let dIter = Math.round(facPerm/1000)
    itin = fac_to_itin.fac_to_itin(n, iter)
    # flag used to determine whether or not memo can be used
    are_same = True
    for i in range(len(itin)):
      index = itin[i]
      are_same = are_same and memo and len(memo) > i and memo[i][0] == index
      #  ... if existing element in memo cannot be used, then reassign it
      if not are_same:
        pair = [index, distance_tot + inter_town_distances[index_last][index]]
        if len(memo) > i:
          memo[i] = pair
        else:
          memo.append(pair)
      distance_tot = memo[i][1]
      index_last = index
    # salesperson ends at the origin, which is n-th point.
    distance_tot += inter_town_distances[index_last][n]
    itin.insert(0, n)
    itin.append(n)
    if distance_tot < distance_min:
      return {"iter": iter, "itin": itin, "distance_min": distance_tot, "memo": memo, "finished": False}
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

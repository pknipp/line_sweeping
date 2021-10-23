# from . import fac_to_itin
# from . import base2_to_ends
from . import helper

def find_one(n, fac_perm, base2_max, iter, base2, distance_min, memo, lines, origin, distances):
    # print("distances = ", distances)
  # loop over all permutations & powers of 2 (ie, all possible itineraries)
    base2 = 0
    itin = helper.fac_to_itin(n, fac_perm, iter)
    # print("iter/itin = ", iter, itin)
    while base2 < base2_max:
      # print("top of base2/while")
      ends = helper.base2_to_ends(n, base2)
      # print("base2/ends = ", base2, ends)
      distance_tot = 0
      # distance from origin to start of zero-th line
      start = lines[itin[0]][ends[0]]
      this_distance = distances[itin[0]][n][ends[0]][0]
      print("0th leg: ", start, origin, this_distance)
      distance_tot += this_distance
      # print("distance after starting leg = ", distance_tot)
      # distance from end of last line back to origin
      start = lines[itin[n - 1]][1 - ends[n - 1]]
      this_distance = distances[itin[n-1]][n][1 - ends[n - 1]][0]
      print("last leg: ", start, origin, this_distance)
      distance_tot += this_distance
      # print("distance after inclusion of ending leg = ", distance_tot)
      index_last = itin[0]
      for i in range(1, len(itin)):
        # print("i/distance_tot = ", i, distance_tot)
        index = itin[i]
        # print("index_last/index/ends[index_last]/[1 - ends[index] = ", index_last, index, ends[index_last], 1 - ends[index])
        start = lines[itin[index_last]][ends[index_last]]
        end   = lines[itin[index     ]][1 - ends[index]]
        this_distance = distances[index_last][index][ends[index_last]][1 - ends[index]]
        print(i,"-th leg: ", start, end, this_distance)
        distance_tot += this_distance
        # print("distance after inclusion of intermediate legs and i = ", i, distance_tot)
      # print("distance_tot/distance_min = ", distance_tot, distance_min)
      if distance_tot < distance_min:
        distance_min = distance_tot
        print("distance_min = ", distance_min)
      base2 += 1
    iter += 1

        # print("Origin is ", origin)
        # for i_line in range(len(lines)):
          # j = itin[i_line]
          # print(lines[j][ends[j]])
        # print("Destination is ", origin)

    # flag used to determine whether or not memo can be used
    # are_same = True
    # for i in range(len(itin)):
      # index = itin[i]
      # are_same = are_same and memo and len(memo) > i and memo[i][0] == index
      #  ... if existing element in memo cannot be used, then reassign it
      # if not are_same:
        # pair = [index, distance_tot + inter_town_distances[index_last][index]]
        # if len(memo) > i:
          # memo[i] = pair
        # else:
          # memo.append(pair)
      # distance_tot = memo[i][1]
      # index_last = index
    # salesperson ends at the origin, which is n-th point.
    # distance_tot += inter_town_distances[index_last][n]
    # itin.insert(0, n)
    # itin.append(n)
    # Return if you find the next minimum of the search.
    # if distance_tot < distance_min:
      # return {"iter": iter, "itin": itin, "distance_min": distance_tot, "memo": memo, "finished": False}
    # Return to provide an update on progress (the next 5%).
    # if not iter % d_iter:
      # return {"iter": iter, "finished": False}
    # iter += 1
  #  return {"finished": True}

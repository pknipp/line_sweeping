let facToItin = require('./facToItin');

const findOne = (n, iter, distanceMin, memo, xys, interTownDistances) => {
  let facPerm = 1;
  for (let i = 1; i <= n; i++) facPerm *= i;
  // loop over all permutations (ie, all possible itineraries)
  while (iter < facPerm) {
    // salesperson starts at origin, which n-th point (0-based indexing) is defined to be.
    let indexLast = n;
    let distanceTot = 0;
    // let dIter = Math.round(facPerm/1000);
    let itin = facToItin(n, iter);
    // flag used to determine whether or not memo can be used
    let areSame = true;
    for (let i = 0; i < itin.length; i++) {
      const index = itin[i];
      areSame = areSame && memo.length && memo[i] && memo[i][0] === index;
      // ... if existing element in memo cannot be used, then reassign it
      if (!areSame) memo[i] = [index, distanceTot + interTownDistances[indexLast][index]];
      distanceTot = memo[i][1];
      indexLast = index;
    }
    // salesperson ends at the origin, which is n-th point.
    distanceTot += interTownDistances[indexLast][n];
    itin.unshift(n);
    itin.push(n);
    if (distanceTot < distanceMin) {
      distanceMin = distanceTot;
      return {iter, itin, distanceMin, finished: false}
    }
    iter++;
    // Break in order to display the next 0.1% of progress.
    // Before both loops, dIter was defined to be Math.round(facPerm/1000)
    // if (!(iterPerm % dIter)) {
      // setNextIterPermI(iterPerm + 1);
      // break;
    // }
    // The loop is done.
    // if (iterPerm === facPerm - 1) {
      // setDone(true);
      // setNextIterPermI(iterPerm);
    // }
  }
  return {finished: true}
}

module.exports = findOne;

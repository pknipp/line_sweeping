let setTowns = require('./setTowns');
let lookup = require('./lookup');
let findOne = require('./findOne');

const tsp = n => {
  let distanceMin = Infinity;
  // let the origin be the n-th town (using 0-based indexing)
  const xys = [...setTowns(n), [0, 0]];
  const interTownDistances = lookup(xys);
  let iter = -1;
  let finished = false;
  let memo = [];
  let itin;
  while (!finished) {
    let results = findOne(n, iter + 1, distanceMin, memo, xys, interTownDistances);
    if (results.finished) break;
    iter = results.iter;
    itin = results.itin,
    distanceMin = results.distanceMin;
    console.log(iter, itin.join("-"), distanceMin);
  }
  console.log("finished");
}

console.log(tsp(9));

module.exports = tsp;

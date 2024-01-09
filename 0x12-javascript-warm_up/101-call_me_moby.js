#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let d = 0; d < x; d++) {
    theFunction();
  }
};

#!/usr/bin/node
/**
 * function that executes x times a function.
 *
 * Run `./mainttest/101-main.js` to test
 */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

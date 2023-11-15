#!/usr/bin/node
/**
 * function that increments and calls a function
 *
 * Run `./mainttest/102-main.js` to test
 */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};

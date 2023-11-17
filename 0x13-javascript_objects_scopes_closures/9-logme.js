#!/usr/bin/node
/**
 * prints the number of arguments already printed and the new argument value
 * @param {*} item
 *
 * Run `./maintest/9-main.js` to test
 */
exports.logMe = function logMe (item) {
  if (!logMe.count) {
    logMe.count = 0;
  }
  console.log(`${logMe.count}: ${item}`);
  logMe.count++;
};

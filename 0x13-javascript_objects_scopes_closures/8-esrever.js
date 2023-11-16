#!/usr/bin/node
/**
 * function that returns the reversed version of a list
 * @param {*} list
 * 
 * Run `./maintest/8-main.js` to test
 */
exports.esrever = function (list) {
  const reversedArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedArray.push(list[i]);
  }
  return reversedArray;
};

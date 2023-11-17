#!/usr/bin/node
/**
 * converts a number from base 10 to another base passed as argument
 * @param {*} base base number
 * @returns another base
 */
exports.converter = function (base) {
  return x => x.toString(base);
};

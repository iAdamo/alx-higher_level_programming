#!/usr/bin/node
/**
 * A class `Square` that inherits from `Rectangle` of 4-rectangle.js
 *
 * Run `./maintest/3-main.js` to test
 */
// importing class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

// exporting the class
module.exports = Square;

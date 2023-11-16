#!/usr/bin/node
/**
 * A class `Square` that inherits from `Rectangle` of 4-rectangle.js
 *
 * Run `./maintest/3-main.js` to test
 */
// importing class
const squareRep = require('./5-square');

class Square extends squareRep {
  // prints the rectangle using the character `c`
  // If c is undefined, use the character `X`
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.charPrint('X');
    }
  }
}

// exporting the class
module.exports = Square;

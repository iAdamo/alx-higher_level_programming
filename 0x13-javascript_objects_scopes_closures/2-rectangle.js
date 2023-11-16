#!/usr/bin/node
/**
 * A class `Rectangle` that defines a rectangle
 *
 * Run `./maintest/1-main.js` to test
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

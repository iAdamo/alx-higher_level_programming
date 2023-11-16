#!/usr/bin/node
/**
 * A class `Rectangle` that defines a rectangle
 *
 * Run `./maintest/3-main.js` to test
 */
class Rectangle {
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle using the character `X`
  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  // exchanges the width and the height of the rectangle
  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  // exchanges the width and the height of the rectangle
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

// exporting the class
module.exports = Rectangle;

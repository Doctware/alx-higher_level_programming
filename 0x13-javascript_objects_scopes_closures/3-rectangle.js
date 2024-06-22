#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    if (this.width !== undefined && this.height !== undefined) {
      for (let ch = 0; ch <= this.height; ch++) {
        console.log('x'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;

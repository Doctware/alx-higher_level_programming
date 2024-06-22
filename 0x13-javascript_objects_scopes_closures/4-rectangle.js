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

  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width !== undefined && this.height !== undefined) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;

#!/usr/bin/node
// the variaables included
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let d = 0; d < this.height; d++) console.log('X'.repeat(this.width));
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};

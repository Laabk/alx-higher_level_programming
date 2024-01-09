#!/usr/bin/node
// this includes the parameters provided

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
  print () {
    for (let d = 0; d < this.height; d++) console.log('X'.repeat(this.width));
  }
};

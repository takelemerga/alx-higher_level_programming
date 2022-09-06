#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let k = 0; k < this.height; k++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;

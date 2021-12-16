#!/usr/bin/node

const sq = require('./5-square.js');

class Square extends sq {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i += 1) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;

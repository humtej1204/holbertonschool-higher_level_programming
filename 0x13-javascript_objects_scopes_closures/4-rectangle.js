#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    const row = new Array(this.width);
    row.fill(c);
    for (let j = 0; j < this.height; j++) console.log(row.join(''));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}

module.exports = Rectangle;

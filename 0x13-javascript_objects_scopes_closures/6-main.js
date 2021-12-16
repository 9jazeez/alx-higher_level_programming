#!/usr/bin/node

const Rec = require('./6-square');

const r1 = new Rec(4, 5);
console.log(r1);
r1.print();
r1.rotate();
console.log(r1);
r1.double();
console.log(r1);
r1.charPrint('$')

const r2 = new Rec(3, 3);
console.log(r2);
r2.double();
r2.charPrint();

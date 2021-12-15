#!/usr/bin/node

const size = process.argv[2];
let shape = '';
for (let i = 0; i < size; i = 1 + i) {
  for (let j = 0; j < size; j += 1) {
    shape += 'X';
  }
  console.log(shape);
  shape = '';
}

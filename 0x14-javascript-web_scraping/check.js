#!/usr/bin/node

const obj1 = { 1: 0, 2: 0, 3: 0 };
for (let i = 1; i < 3; i++) {
  obj1[i] = obj1[i] + 1;
}

console.log(obj1);

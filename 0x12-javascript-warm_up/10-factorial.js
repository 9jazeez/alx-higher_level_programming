#!/usr/bin/node

function fact (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  } else {
    return (a * fact(a - 1));
  }
}

const num = parseInt(process.argv[2]);
const res = fact(num);
console.log(res);

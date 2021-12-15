#!/usr/bin/node

const myVar = process.argv;
if (myVar[2]) {
  console.log(myVar[2]);
} else {
  console.log('No argument');
}
// console.log(myVar[2]);

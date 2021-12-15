#!/usr/bin/node

let myVar = process.argv[2];
myVar = parseInt(myVar);
if (isNaN(myVar)) {
  console.log('Not A Number');
} else {
  console.log(myVar);
}

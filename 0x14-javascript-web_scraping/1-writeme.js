#!/usr/bin/node

const file = require('fs');
const fileName = process.argv[2];
const str = process.argv[3];

file.writeFile(fileName, str, 'utf-8', function (err) {
  if (err) throw err;
  console.log('Written');
});

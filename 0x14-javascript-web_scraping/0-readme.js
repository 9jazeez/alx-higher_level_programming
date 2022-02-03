#!/usr/bin/node

const file = require('fs');

file.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (data) {
    if (data === null) {
      process.stdout.write('Empty');
    } else {
      process.stdout.write(data);
    }
  } else {
    console.log(err);
  }
});

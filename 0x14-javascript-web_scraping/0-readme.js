#!/usr/bin/node

const file = require('fs');

file.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});

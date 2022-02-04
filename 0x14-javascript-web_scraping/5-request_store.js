#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(res.statusCode);
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      } else {
        console.log('Written');
      }
    });
  }
});

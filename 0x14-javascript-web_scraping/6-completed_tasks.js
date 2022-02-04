#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const output = JSON.parse(body);
    const dict = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
      7: 0,
      8: 0,
      9: 0,
      10: 0
    };
    for (let i = 0; i < output.length; i++) {
      if (output[i].completed === true) {
        const value = output[i].userId;
        dict[value] = dict[value] + 1;
      }
    }
    console.log(dict);
  }
});

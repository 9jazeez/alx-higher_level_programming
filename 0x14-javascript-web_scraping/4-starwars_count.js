#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films';

request(url, function (error, response, body) {
  if (error) {
    console.error('error:' + error);
  } else {
    let result = JSON.parse(body);
    result = result.results;
    let count = 0;

    for (let i = 0; i < result.length; i++) {
      const character = result[i].characters;
      for (let b = 0; b < character.length; b++) {
        const str = character[b];
        if (str.includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:' + error);
  } else {
    let title = JSON.parse(body);
    title = title.title;
    console.log(title);
  }
});

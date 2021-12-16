#!/usr/bin/node

const converter = require('./10-converter').converter;

let conv = converter(2);
console.log(conv(2));
console.log(conv(4));

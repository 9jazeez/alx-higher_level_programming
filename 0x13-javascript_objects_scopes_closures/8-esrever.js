#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  for (const element of list) {
    result.unshift(element);
  }
  return result;
};

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((i, value) => i + (value === searchElement), 0);
  return count;
};

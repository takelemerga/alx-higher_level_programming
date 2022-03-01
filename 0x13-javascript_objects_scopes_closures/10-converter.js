#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    return num.toString(base);
  };
};

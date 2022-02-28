#!/usr/bin/node
const args = require('process');

const arg = parseInt(args.argv[2]);
console.log(factorial(arg));

function factorial (a) {
  if (!a) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

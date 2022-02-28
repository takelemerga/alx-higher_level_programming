#!/usr/bin/node
const args = require('process');
const arg2 = parseInt(args.argv[2]);
if (isNaN(arg2)) {
  console.log('Missing number of occurrences');
} else {
  let j = 0;
  while (j < arg2) {
    console.log('C is fun');
    j++;
  }
}

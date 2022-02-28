#!/usr/bin/node
const args = require('process');
const arg1 = parseInt(args.argv[2]);
if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  let j = 0;
  while (j < arg1) {
    console.log('X'.repeat(arg1));
    j++;
  }
}

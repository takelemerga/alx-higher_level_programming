#!/usr/bin/node

const args = require('process');
const arg2 = parseInt(args.argv[2]);
if (isNaN(arg2)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg2);
}

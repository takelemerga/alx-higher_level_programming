#!/usr/bin/node
const args = require('process');
add(args.argv[2], args.argv[3]);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

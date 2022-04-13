#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const writeme = process.argv[3];

fs.writeFile(file, writeme, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});

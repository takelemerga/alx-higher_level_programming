#!/usr/bin/node

const dict = require('./101-data').dict;
const dicti = {};
for (const key in dict) {
  if (dict[key] in dicti) {
    dicti[dict[key]] = dicti[dict[key]].concat([key]);
  } else {
    dicti[dict[key]] = [key];
  }
}
console.log(dicti);

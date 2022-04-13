#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const request = require('request');
const url = process.argv[2];

function numMovies (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let count = 0;
      const hasId = /18/;
      const resList = JSON.parse(body).results;
      for (let i = 0; i < resList.length; i++) {
        const chars = resList[i].characters;
        for (let j = 0; j < chars.length; j++) {
          if (hasId.test(chars[j]) === true) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
numMovies(url);
